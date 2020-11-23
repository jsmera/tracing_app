from django.contrib import admin
from .models import Adoption
from .forms import CreateAdoptionForm


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    form = CreateAdoptionForm
    add_form = CreateAdoptionForm
    list_display = ["adopter", "pet", "date"]
    search_fields = ["date"]
