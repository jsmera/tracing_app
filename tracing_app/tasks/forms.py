from django.forms import ModelForm
from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from django.core.validators import FileExtensionValidator
from crispy_forms.layout import Submit


class BaseCrispy(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit("submit", "Guardar"))


class CreateTaskForm(BaseCrispy):
    class Meta:
        model = Task
        fields = [
            "type",
            "status",
            "adopcion",
        ]
        widgets = {
            "adopcion": forms.HiddenInput(),
        }


class CreateReminderForm(BaseCrispy):
    type = forms.ChoiceField(
        choices=[("reminder", "Recordatorio")], widget=forms.HiddenInput()
    )
    text = forms.CharField(label="Recordatorio", required=True)

    class Meta:
        model = Task
        fields = [
            "type",
            "status",
            "text",
            "adopcion",
        ]
        widgets = {
            "adopcion": forms.HiddenInput(),
        }


class EditTaskForm(BaseCrispy):
    class Meta:
        model = Task
        fields = [
            "status",
        ]


class CompleteMultimediaTask(BaseCrispy):
    file_path = forms.FileField(
        required=True,
        label="Imagen o video de tu peludo",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "png", "jpeg", "mp4", "mov", "avi"],
                message="Sube alguna imagen o video.",
            )
        ],
    )

    class Meta:
        model = Task
        fields = [
            "status",
            "file_path",
        ]
        widgets = {
            "status": forms.HiddenInput(),
        }


class CompleteTextTask(BaseCrispy):
    text = forms.CharField(
        required=True,
        max_length=500,
        label="Cuentanos como te va...",
        widget=forms.Textarea(),
    )

    class Meta:
        model = Task
        fields = [
            "status",
            "text",
        ]
        widgets = {
            "status": forms.HiddenInput(),
        }