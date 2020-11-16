from django.forms import ModelForm
from django import forms
from .models import  Adoption


class CreateAdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = [
            "date",
            "status",
            "adopter",
            "pet",
        ]

