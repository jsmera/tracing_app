from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdoptionConfig(AppConfig):
    name = 'tracing_app.adoptions'
    verbose_name = _("Adoptions")

