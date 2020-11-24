from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from tracing_app.adoptions.models import Adoption
from .models import Task, Configuration
from .forms import (
    CreateTaskForm,
    CompleteMultimediaTask,
    CompleteTextTask,
    EditTaskForm,
    CreateReminderForm,
    ConfigurationTaskForm,
    ConfigurationReminderForm,
    EditConfigurationTaskForm,
    EditConfigurationReminderForm,
)
from django.views.generic.base import TemplateView
from django.http import Http404
from .tasks import send_notification, create_notifications
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreateView(LoginRequiredMixin, CreateView):
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

    def form_valid(self, form):
        url = super(TaskCreateView, self).form_valid(form)
        create_notifications(self.object.id)
        return url

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


class NotifyView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pid = kwargs["task"]
        task = get_object_or_404(Task, id=pid)
        send_notification(task.id)

        return redirect(reverse("tasks:task-edit", args=(task.adopcion.id, task.id)))


class TaskUpdateView(LoginRequiredMixin, UpdateView):
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


class ConfigurationsListView(LoginRequiredMixin, ListView):
    model = Configuration


class ConfigurationTaskCreateView(LoginRequiredMixin, CreateView):
    model = Configuration
    form_class = ConfigurationTaskForm

    def get_success_url(self):
        return reverse("tasks:config-list")


class ConfigurationReminderCreateView(ConfigurationTaskCreateView):
    form_class = ConfigurationReminderForm

    def get_form_kwargs(self):
        kwargs = super(ConfigurationReminderCreateView, self).get_form_kwargs()
        if "data" in kwargs:
            data = kwargs["data"].copy()
            data.appendlist("type", "reminder")
            kwargs["data"] = data
        return kwargs

    def get_success_url(self):
        return reverse("tasks:config-list")


class ConfigurationsUpdateView(LoginRequiredMixin, UpdateView):
    model = Configuration

    def get_success_url(self):
        return reverse("tasks:config-list")

    def get_form_class(self):
        task = self.object
        if task.type in ["multimedia", "text"]:
            return EditConfigurationTaskForm
        elif task.type == "reminder":
            return EditConfigurationReminderForm
        else:
            return super(ConfigurationsUpdateView, self).get_form_class()
