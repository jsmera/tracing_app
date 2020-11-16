# Generated by Django 3.0.10 on 2020-11-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefono')),
                ('other_phone', models.CharField(blank=True, max_length=50, verbose_name='Otro telefono')),
                ('address', models.CharField(max_length=100, verbose_name='Direccion')),
                ('id_document', models.CharField(max_length=20, verbose_name='Numero de documento')),
                ('gender', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], default='M', max_length=2, verbose_name='Genero')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('type_document', models.CharField(choices=[('CC', 'Cedula'), ('TI', 'Tarjeta de identidad')], default='CC', max_length=2, verbose_name='Tipo de documento')),
            ],
        ),
    ]