from django import forms
from .models import Registro


class TaskForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('nome', 'cpf', 'aluguel', 'status', 'atraso', 'tamanho')


