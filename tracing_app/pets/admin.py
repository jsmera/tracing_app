from django.contrib import admin
from .models import  Pet
from .forms import  CreatePetForm



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    form = CreatePetForm
    add_form = CreatePetForm
    list_display = ["code", "name", "age"]
    search_fields = ["name"]

