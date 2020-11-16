from django.forms import ModelForm
from django import forms
from .models import Adopter


class CreateAdopterForm(ModelForm):
    class Meta:
        model = Adopter
        fields = [
            "first_name",
            "last_name",
            "gender",
            "type_document",
            "id_document",
            "address",
            "email",
            "phone",
            "other_phone",
        ]
