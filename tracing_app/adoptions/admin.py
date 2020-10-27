from django.contrib import admin
from .models import Adopter, Pet, Adoption
from .forms import CreateAdopterForm, CreatePetForm, CreateAdoptionForm


@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    form = CreateAdopterForm
    add_form = CreateAdopterForm
    list_display = ["first_name", "type_document", "id_document", "email", "phone"]
    search_fields = ["first_name"]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    form = CreatePetForm
    add_form = CreatePetForm
    list_display = ["code", "name", "age"]
    search_fields = ["name"]


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    form = CreateAdoptionForm
    add_form = CreateAdoptionForm
    list_display = ["adopter", "pet", "date"]
    search_fields = ["date"]
