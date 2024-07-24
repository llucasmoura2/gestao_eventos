from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime
from django.views import View
from .api_models import Mensagem  # modelo da msg


class ScheduleMessageView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        mensagem = data.get('mensagem')
        data_envio = data.get('data_envio')
        hora_envio = data.get('hora_envio')

        try:           
            data_envio = datetime.strptime(data_envio, '%d-%m-%Y').date()
            hora_envio = datetime.strptime(hora_envio, '%H:%M:%S').time()
        except ValueError:
            return JsonResponse({'status': 'Formato de data ou hora inválido.'}, status=400)

        # Cria e salva mensagem agendada
        nova_mensagem = Mensagem(mensagem=mensagem, data_envio=data_envio, hora_envio=hora_envio)
        nova_mensagem.save()

        return JsonResponse({'status': 'Mensagem agendada com sucesso!'})

        
@csrf_exempt
def agendar_mensagem(request):
    if request.method == "POST":
        data = request.POST
        mensagem = data.get('mensagem')
        data_envio = data.get('data_envio')
        hora_envio = data.get('hora_envio')

        try:           
            data_envio = datetime.strptime(data_envio, '%d-%m-%Y').date()
            hora_envio = datetime.strptime(hora_envio, '%H:%M:%S').time()
        except ValueError:
            return JsonResponse({'status': 'Formato de data ou hora inválido.'}, status=400)

        # cria e salva msg agendada
        nova_mensagem = Mensagem(mensagem=mensagem, data_envio=data_envio)
        nova_mensagem.save()

        return JsonResponse({'status': 'Msg agendada com sucesso, Hd!'})

    return JsonResponse({'status': 'Método não permitido.'}, status=405)
