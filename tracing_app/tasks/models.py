from django.db import models
from django.utils import timezone


class Task(models.Model):
    STATUS = [("inprogress", "En progreso"), ("finished", "Finalizada")]
    typeT = models.CharField(max_length=50, unique=True, verbose_name="tipo")
    date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de inicio")
    periodic = models.BooleanField(default=False, verbose_name = "periodica")
    file_path = models.CharField(max_length=50, verbose_name="ruta archivo")
    status = models.CharField(
        verbose_name="Estado de tarea",
        choices=STATUS,
        max_length=11,
        default="inprogress",
    )
    date_end = models.DateTimeField(default=timezone.now, verbose_name="Fecha de finalizacion")
    adopcion = models.ForeignKey("adoptions.Adoption", default=1, on_delete=models.PROTECT, verbose_name="Adopcion")


