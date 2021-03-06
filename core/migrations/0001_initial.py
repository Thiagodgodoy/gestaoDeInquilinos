# Generated by Django 4.0.3 on 2022-03-24 20:08

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='CPF')),
                ('aluguel', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor do aluguel')),
            ],
        ),
    ]
