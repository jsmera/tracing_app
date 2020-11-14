from django.forms import ModelForm
from django import forms
from .models import Pet


class CreatePetForm(ModelForm):
    class Meta:
        model = Pet
        fields = [
            "code",
            "name",
            "age",
            "disability",
            "comments",
        ]

