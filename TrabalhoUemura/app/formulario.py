from django import forms
from .models import Tarefas

class Formulario_de_tarefas(forms.ModelForm):
    class Meta:
        modelo = Tarefas
        descricao_tarefas = ['titulo', 'descricao', 'status', 'responsavel_por']