from django.db import models
from django.utils import timezone


class Adopter(models.Model):
    TYPE_DOCUMENT = [("CC", "Cedula"), ("TI", "Tarjeta de identidad")]
    GENDER = [("F", "Femenino"), ("M", "Masculino"), ("O", "Otro")]
    first_name = models.CharField(max_length=30, verbose_name="Nombres")
    last_name = models.CharField(max_length=150, verbose_name="Apellidos")
    phone = models.CharField(max_length=50, verbose_name="Telefono")
    other_phone = models.CharField(max_length=50, blank=True, verbose_name="Otro telefono",)
    address = models.CharField(max_length=100, verbose_name="Direccion",)
    id_document = models.CharField(max_length=20, verbose_name="Numero de documento",)
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default="M",
        verbose_name="Genero",
    )
    email = models.EmailField(
        max_length=254, verbose_name="Correo electrónico"
    )
    type_document = models.CharField(
        verbose_name="Tipo de documento",
        max_length=2, choices=TYPE_DOCUMENT, default="CC",
    )

    def __str__(self):
        return f"{self.first_name} - {self.id_document}"

class Pet(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Codigo")
    name = models.CharField(max_length=30, verbose_name="Nombre")
    age = models.PositiveSmallIntegerField(verbose_name="Edad")
    disability = models.BooleanField(default=False, verbose_name="Discapacidad")
    comments = models.TextField(verbose_name="Comentarios")

    def __str__(self):
        return f"{self.name} - {self.age} años"


class Adoption(models.Model):
    STATUS = [("inprogress", "En progreso"), ("cancelled", "Cancelada"), ("inreview", "En revision"), ("finished", "Finalizada")]
    date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de adopcion")
    status = models.CharField(
        verbose_name="Estado de adopcion",
        choices=STATUS,
        max_length=11,
        default="inprogress",
    )
    adopter = models.ForeignKey("Adopter", on_delete=models.PROTECT, verbose_name="Adoptante")
    pet = models.ForeignKey("Pet", on_delete=models.PROTECT, verbose_name="Mascota")
