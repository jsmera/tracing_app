# Generated by Django 3.0.10 on 2020-10-27 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adopter',
            old_name='type_documento',
            new_name='type_document',
        ),
    ]
