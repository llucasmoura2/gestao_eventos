from django.db import models


TIPO_CHAVE_CHOICES = [
    ('cel', 'Celular'),
    ('cnpj', 'CNPJ'),
    ('email', 'E-mail'),
    ('cpf', 'CPF'),
]

class Artista(models.Model):

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, null=True)
    banco = models.CharField(max_length=100)
    tipo_chave_pix = models.CharField(max_length=10, choices=TIPO_CHAVE_CHOICES, default='cel')
    chave_pix = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
