from django.forms import ModelForm
from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from .models import Pet


class BaseCrispy(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit("submit", "Guardar"))


class CreatePetForm(BaseCrispy):
    class Meta:
        model = Pet
        fields = [
            "name",
            "age",
            "disability",
            "comments",
        ]
