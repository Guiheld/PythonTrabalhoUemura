from django import forms
from .models import Tarefas

class Formulario_de_tarefas(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['titulo', 'descricao', 'status', 'tarefa_atribuida']
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'status': forms.Select(choices=Tarefas.Definicao_status),
            'tarefa_atribuida': forms.Select(),  # Renderizar como select
        }