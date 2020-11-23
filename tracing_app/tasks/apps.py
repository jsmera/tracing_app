from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TasksConfig(AppConfig):
    name = "tracing_app.tasks"
    verbose_name = _("Tasks")
