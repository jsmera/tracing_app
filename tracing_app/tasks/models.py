import uuid
from django.db import models
from django.utils import timezone


def task_directory_path(instance, filename):
    return "task_{0}/{1}".format(instance.uuid, filename)


class Task(models.Model):
    STATUS = [
        ("inprogress", "En progreso"),
        ("canceled", "Cancelada"),
        ("finished", "Finalizada"),
        ("expired", "Expirada"),
    ]
    TYPE = [
        ("multimedia", "Registro multimedia"),
        ("text", "Registro texto"),
        ("reminder", "Recordatorio"),
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    type = models.CharField(
        verbose_name="Tipo de tarea",
        choices=TYPE,
        max_length=11,
        default="multimedia",
    )
    file_path = models.FileField(blank=True, null=True, upload_to=task_directory_path)
    text = models.TextField(blank=True, max_length=500)
    status = models.CharField(
        verbose_name="Estado de tarea",
        choices=STATUS,
        max_length=11,
        default="inprogress",
    )
    date_start = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de inicio"
    )
    date_end = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de finalizacion"
    )
    adopcion = models.ForeignKey(
        "adoptions.Adoption",
        default=1,
        on_delete=models.PROTECT,
        verbose_name="Adopcion",
    )

    def __str__(self):
        return f"Tarea de tipo: {self.get_type_display()}. Estado: {self.get_status_display()}"


class Configuration(models.Model):
    TYPE = [
        ("multimedia", "Registro multimedia"),
        ("text", "Registro texto"),
        ("reminder", "Recordatorio"),
    ]
    UNIT = [("days", "Dias"), ("weeks", "Semanas"), ("months", "Meses")]
    type = models.CharField(
        verbose_name="Tipo de tarea",
        choices=TYPE,
        max_length=11,
        default="multimedia",
    )
    unit = models.CharField(
        verbose_name="Unidad de tiempo",
        choices=UNIT,
        max_length=7,
        default="weeks",
    )
    delta_difference = models.IntegerField(
        verbose_name="Tiempo",
        help_text=(
            "Ejemplo: Tarea a realizar 1 semana despues de la fecha de adopción."
        ),
        default=1,
    )
    text = models.TextField(blank=True, max_length=500)

    def __str__(self):
        complete = f"{self.delta_difference} {self.get_unit_display().lower()} despues de la fecha de adopción"
        if self.type == "reminder":
            return f"Recordatorio {complete}"
        else:
            return f"Tarea de tipo {self.get_type_display().lower()} {complete}"
