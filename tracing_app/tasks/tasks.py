from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
from django.urls import reverse
from config.celery_app import app
from django_celery_beat.models import PeriodicTask, ClockedSchedule
from datetime import timedelta
from .models import Task, Configuration
from tracing_app.adoptions.models import Adoption
import json


def get_absolute_site_url():
    return "https://%s" % (Site.objects.get_current().domain)


@app.task
def send_notification(task_id):
    task = Task.objects.get(id=task_id)
    adoption = task.adopcion
    adopter = adoption.adopter
    context = {
        "task": task,
        "adopter": adopter,
        "url": "{}{}".format(
            get_absolute_site_url(),
            reverse("tasks:public-task", args=(task.uuid,)),
        ),
    }
    html_message = render_to_string("emails/notification.html", context)
    if task.type != "reminder":
        subject = "Nueva tarea para ti y tu mascota!"
    else:
        subject = "Recordatio: {}".format(task.text)

    valid = send_mail(
        subject,
        html_message,
        settings.DEFAULT_FROM_EMAIL,
        [adopter.email],
        fail_silently=False,
        html_message=html_message,
    )
    return valid


@app.task
def create_notifications(task_id):
    task = Task.objects.get(id=task_id)
    dates = []
    for days in [-7, -2, 0]:
        pivot = task.date_start + timedelta(days=days)
        dates.append(pivot.replace(hour=8, minute=0, second=0))
    for date in dates:
        clocked = ClockedSchedule.objects.create(
            clocked_time=date,
        )
        PeriodicTask.objects.create(
            name=f"Notificación para {task_id} en {date}",
            task="tracing_app.tasks.tasks.send_notification",
            clocked=clocked,
            kwargs=json.dumps(
                {
                    "task_id": task.id,
                }
            ),
            one_off=True,
        )


MAPPER = {
    "days": 1,
    "weeks": 7,
    "months": 30,
}


@app.task
def create_tasks(adoption_id):
    adoption = Adoption.objects.get(id=adoption_id)
    configs = Configuration.objects.all()
    for config in configs:
        days = config.delta_difference * MAPPER[config.unit]
        pivot = adoption.date + timedelta(days=days)
        date_start = pivot.replace(hour=8, minute=0, second=0)
        date_end = date_start + timedelta(days=7)
        task = Task.objects.create(
            type=config.type,
            text=config.text,
            date_start=date_start,
            date_end=date_end,
            adopcion=adoption,
        )
        create_notifications.apply((task.id,))
