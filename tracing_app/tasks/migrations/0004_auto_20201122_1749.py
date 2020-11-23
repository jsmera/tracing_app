# Generated by Django 3.0.10 on 2020-11-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_task_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="text",
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="task",
            name="file_path",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Ruta archivo"
            ),
        ),
    ]