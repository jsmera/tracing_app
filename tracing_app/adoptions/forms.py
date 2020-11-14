from django.forms import ModelForm
from django import forms
from .models import Adopter, Pet, Task, Adoption


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


class CreateAdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = [
            "date",
            "status",
            "adopter",
            "pet",
        ]

class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "typeT",
            "date",
            "periodic", 
            "file_path",
            "status",
            "date_end",
            "adopcion",
        ]
