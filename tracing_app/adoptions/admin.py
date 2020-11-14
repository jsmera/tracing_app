from django.contrib import admin
from .models import Adopter, Adoption
from .forms import CreateAdopterForm,  CreateAdoptionForm


@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    form = CreateAdopterForm
    add_form = CreateAdopterForm
    list_display = ["first_name", "type_document", "id_document", "email", "phone"]
    search_fields = ["first_name"]





@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    form = CreateAdoptionForm
    add_form = CreateAdoptionForm
    list_display = ["adopter", "pet", "date"]
    search_fields = ["date"]
