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
    adopcion = models.ForeignKey("Adoption", on_delete=models.PROTECT, verbose_name="Adopcion")


class Adoption(models.Model):
    STATUS = [("inprogress", "En progreso"), ("cancelled", "Cancelada"), ("inreview", "En revision"), ("finished", "Finalizada")]
    date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de adopcion")
    status = models.CharField(
        verbose_name="Estado de adopcion",
        choices=STATUS,
        max_length=11,
        default="inprogress",
    )
    adopter = models.ForeignKey("adopters.Adopter",default=1, on_delete=models.PROTECT, verbose_name="Adoptante")
    pet = models.ForeignKey("pets.Pet", default=1, on_delete=models.PROTECT, verbose_name="Mascota")
    


