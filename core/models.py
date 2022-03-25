from django.db import models
from django.db.models import Model
from cpf_field.models import CPFField
from django.contrib.auth import get_user_model


class Registro(Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
        ('total', 'Total')
    )
    KITNET = (
        ("P", "PEQUENA"),
        ("M", "MEDIA"),
        ("G", "GRANDE")
    )

    nome = models.CharField('Nome', max_length=100)
    cpf = CPFField('CPF')
    aluguel = models.DecimalField('Valor do aluguel', max_digits=12, decimal_places=2)
    tamanho = models.CharField('Tamanho da kitnet', max_length=1, choices=KITNET, blank=False, null=False)
    status = models.BooleanField('Está inadimplente?')
    atraso = models.DecimalField('Quantos meses de inadimplencia?(caso não digite 0)', max_digits=3, decimal_places=0)
    done = models.CharField(max_length=12, choices=STATUS)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
