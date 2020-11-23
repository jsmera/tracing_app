from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PetsConfig(AppConfig):
    name = "tracing_app.pets"
    verbose_name = _("Pets")
