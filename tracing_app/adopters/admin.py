from django.contrib import admin
from .models import Adopter
from .forms import CreateAdopterForm


@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    form = CreateAdopterForm
    add_form = CreateAdopterForm
    list_display = ["first_name", "type_document", "id_document", "email", "phone"]
    search_fields = ["first_name"]
