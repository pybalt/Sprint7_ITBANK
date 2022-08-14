# Generated by Django 4.1 on 2022-08-14 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('Nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('DNI', models.IntegerField(verbose_name='DNI')),
                ('FechaNacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('Email', models.EmailField(max_length=255, verbose_name='Email')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sucursal.sucursal')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
            },
        ),
    ]
