from django.forms import ModelForm
from django import forms
from .models import Adoption
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class BaseCrispy(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit("submit", "Guardar"))


class CreateAdoptionForm(BaseCrispy):
    class Meta:
        model = Adoption
        fields = [
            "date",
            "status",
            "adopter",
            "pet",
        ]


class EditAdoptionForm(BaseCrispy):
    class Meta:
        model = Adoption
        fields = [
            "status",
        ]
