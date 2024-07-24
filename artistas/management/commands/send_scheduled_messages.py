from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from app.api_models import Mensagem  # Altere o import conforme o local do seu modelo
from typebot import send_whatsapp_message  # Supondo que você tenha uma função para enviar mensagens via Typebot

class Command(BaseCommand):
    help = 'Verifica e envia mensagens agendadas'

    def handle(self, *args, **options):
        agora = timezone.now()
        mensagens = Mensagem.objects.filter(data_envio__lte=agora, enviado=False)

        for mensagem in mensagens:
            send_whatsapp_message(mensagem.mensagem)  # Enviar mensagem usando Typebot
            mensagem.enviado = True
            mensagem.save()

        self.stdout.write(self.style.SUCCESS('Mensagens enviadas com sucesso.'))
