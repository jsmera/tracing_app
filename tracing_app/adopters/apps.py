from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdoptersConfig(AppConfig):
    name = "tracing_app.adopters"
    verbose_name = _("Adopters")
