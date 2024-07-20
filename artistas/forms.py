from django import forms
from validate_docbr import CPF
from . import models

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = models.Artista
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'banco': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_chave_pix': forms.TextInput(attrs={'class': 'form-control'}),
            'chave_pix': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf_validator = CPF()
        if not cpf:
            raise forms.ValidationError('Campo CPF é obrigatório.')
        if not cpf_validator.validate(cpf):
            raise forms.ValidationError('Digite um CPF válido.')
        # Formatar o CPF
        formatted_cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return formatted_cpf