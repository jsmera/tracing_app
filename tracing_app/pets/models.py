from django.db import models
from django.utils import timezone


class Pet(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Codigo")
    name = models.CharField(max_length=30, verbose_name="Nombre")
    age = models.PositiveSmallIntegerField(verbose_name="Edad")
    disability = models.BooleanField(default=False, verbose_name="Discapacidad")
    comments = models.TextField(verbose_name="Comentarios")

    def __str__(self):
        return f"{self.name} - {self.age} años"


