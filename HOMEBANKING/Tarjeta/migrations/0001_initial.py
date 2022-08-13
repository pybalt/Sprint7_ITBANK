# Generated by Django 4.1 on 2022-08-12 23:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)], verbose_name='numero_tarjeta')),
                ('cvv', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4)], verbose_name='cvv')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='fecha')),
                ('fecha_expiracion', models.DateField(verbose_name='fecha_expiracion')),
                ('marca', models.CharField(choices=[('V', 'VISA'), ('M', 'MASTERCARD')], max_length=2)),
                ('tipo', models.CharField(choices=[('C', 'Credito'), ('D', 'DEBITO')], max_length=2)),
            ],
            options={
                'verbose_name': 'tarjeta',
                'verbose_name_plural': 'tarjetas',
                'db_table': 'Tarjeta',
            },
        ),
    ]
