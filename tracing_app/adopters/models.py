from django.db import models
from django.utils import timezone


class Adopter(models.Model):
    TYPE_DOCUMENT = [("CC", "Cedula"), ("TI", "Tarjeta de identidad")]
    GENDER = [("F", "Femenino"), ("M", "Masculino"), ("O", "Otro")]
    first_name = models.CharField(max_length=30, verbose_name="Nombres")
    last_name = models.CharField(max_length=150, verbose_name="Apellidos")
    phone = models.CharField(max_length=50, verbose_name="Telefono")
    other_phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Otro telefono",
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Direccion",
    )
    id_document = models.CharField(
        max_length=20,
        verbose_name="Numero de documento",
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default="M",
        verbose_name="Genero",
    )
    email = models.EmailField(max_length=254, verbose_name="Correo electrónico")
    type_document = models.CharField(
        verbose_name="Tipo de documento",
        max_length=2,
        choices=TYPE_DOCUMENT,
        default="CC",
    )

    def __str__(self):
        return f"{self.first_name} - {self.id_document}"
