from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from accounts.views import login_view, logout_view, register_view
from datetime import datetime
from eventos.models import Evento


def home(request):
    current_year = datetime.now().year
    proximos_eventos = Evento.objects.filter(data__gte=datetime.now()).order_by('data')[:5]
    return render(request, 'base.html', {
        'current_year': current_year,
        'eventos_proximos': proximos_eventos,
        'show_proximos_eventos': True,  # Adiciona a variável para controle condicional
    })


urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', home, name='home'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('', include('eventos.urls')),
    path('', include('artistas.urls'))
]
