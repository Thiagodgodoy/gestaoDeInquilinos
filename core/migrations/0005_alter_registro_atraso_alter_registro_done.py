# Generated by Django 4.0.3 on 2022-03-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_registro_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='atraso',
            field=models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Quantos meses de inadimplencia?(caso não digite 0)'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='done',
            field=models.CharField(choices=[('doing', 'Doing'), ('done', 'Done'), ('total', 'Total')], max_length=12),
        ),
    ]
