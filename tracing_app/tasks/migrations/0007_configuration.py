# Generated by Django 3.0.10 on 2020-11-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0006_auto_20201122_2214"),
    ]

    operations = [
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("multimedia", "Registro multimedia"),
                            ("text", "Registro texto"),
                            ("reminder", "Recordatorio"),
                        ],
                        default="multimedia",
                        max_length=11,
                        verbose_name="Tipo de tarea",
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            ("days", "Dias"),
                            ("weeks", "Semanas"),
                            ("months", "Meses"),
                        ],
                        default="weeks",
                        max_length=7,
                        verbose_name="Unidad de tiempo",
                    ),
                ),
                (
                    "delta_difference",
                    models.IntegerField(
                        default=1,
                        help_text="Ejemplo: Tarea a realizar 1 semana despues de la fecha de adopción.",
                        verbose_name="Tiempo",
                    ),
                ),
                ("text", models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
