from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from tracing_app.adoptions.models import Adoption
from .models import Task
from .forms import (
    CreateTaskForm,
    CompleteMultimediaTask,
    CompleteTextTask,
    EditTaskForm,
    CreateReminderForm,
)
from django.views.generic.base import TemplateView
from django.http import Http404
from .tasks import send_notification


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm

    def setup(self, request, *args, **kwargs):
        super(TaskCreateView, self).setup(request, *args, **kwargs)
        self.adoption = get_object_or_404(Adoption, id=self.kwargs["adpotion"])

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        if "data" in kwargs:
            data = kwargs["data"].copy()
            data.appendlist("adopcion", self.adoption)
            kwargs["data"] = data
        return kwargs

    def get_success_url(self):
        return reverse("adoptions:adoption-edit", args=(self.adoption.id,))


class ReminderCreateView(TaskCreateView):
    form_class = CreateReminderForm

    def get_form_kwargs(self):
        kwargs = super(ReminderCreateView, self).get_form_kwargs()
        if "data" in kwargs:
            data = kwargs["data"].copy()
            data.appendlist("type", "reminder")
            kwargs["data"] = data
        return kwargs


class NotifyView(View):
    def post(self, request, *args, **kwargs):
        pid = kwargs["task"]
        task = get_object_or_404(Task, id=pid)
        send_notification(task)

        return redirect(reverse("tasks:task-edit", args=(task.adopcion.id, task.id)))


class TaskUpdateView(UpdateView):
    model = Task
    form_class = EditTaskForm

    def setup(self, request, *args, **kwargs):
        super(TaskUpdateView, self).setup(request, *args, **kwargs)
        self.adoption = get_object_or_404(Adoption, id=self.kwargs["adpotion"])

    def get_success_url(self):
        return reverse("adoptions:adoption-edit", args=(self.adoption.id,))


class CompleteTaskView(UpdateView):
    model = Task
    form_class = CreateTaskForm
    slug_field = "uuid"
    slug_url_kwarg = "uuid"
    template_name = "pages/public.html"

    def get_success_url(self):
        return reverse("tasks:done-task")

    def get_form_kwargs(self):
        kwargs = super(CompleteTaskView, self).get_form_kwargs()
        if "data" in kwargs:
            data = kwargs["data"].copy()
            data.appendlist("status", "finished")
            kwargs["data"] = data
        return kwargs

    def get_form_class(self):
        task = self.object
        if task.type == "multimedia":
            return CompleteMultimediaTask
        elif task.type == "text":
            return CompleteTextTask
        else:
            return super(CompleteTaskView, self).get_form_class()


class DoneTaskView(TemplateView):
    template_name = "pages/done.html"