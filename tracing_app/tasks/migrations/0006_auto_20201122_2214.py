# Generated by Django 3.0.10 on 2020-11-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_auto_20201122_1922"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="text",
            field=models.TextField(blank=True, max_length=500),
        ),
    ]