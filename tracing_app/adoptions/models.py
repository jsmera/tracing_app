from django.db import models
from django.utils import timezone


class Adoption(models.Model):
    STATUS = [
        ("inprogress", "En progreso"),
        ("cancelled", "Cancelada"),
        ("inreview", "En revision"),
        ("finished", "Finalizada"),
    ]
    date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de adopcion")
    status = models.CharField(
        verbose_name="Estado de adopcion",
        choices=STATUS,
        max_length=11,
        default="inprogress",
    )
    adopter = models.ForeignKey(
        "adopters.Adopter",
        default=1,
        on_delete=models.PROTECT,
        verbose_name="Adoptante",
    )
    pet = models.ForeignKey(
        "pets.Pet", default=1, on_delete=models.PROTECT, verbose_name="Mascota"
    )

    def __str__(self):
        return f"{self.adopter.first_name} adopto a {self.pet}. Estado: {self.get_status_display()}"
