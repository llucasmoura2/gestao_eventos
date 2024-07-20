from django import forms
from .models import Evento, Artista

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['artista', 'data', 'horario', 'descricao']
        widgets = {
            'artista': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }