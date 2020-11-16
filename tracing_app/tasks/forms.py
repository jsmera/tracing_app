from django.forms import ModelForm
from django import forms
from .models import  Task

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
