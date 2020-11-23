from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
from django.urls import reverse


def get_absolute_site_url():
    return "https://%s" % (Site.objects.get_current().domain)


def send_notification(task):
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
