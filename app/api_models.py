from django.db import models
from django.utils import timezone

class Mensagem(models.Model):
    mensagem = models.TextField()
    data_envio = models.DateTimeField()
    hora_envio = models.TimeField()
    enviado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Mensagem para {self.data_envio}"