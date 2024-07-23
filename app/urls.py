#url principal
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from accounts.views import login_view, logout_view, register_view
from django.views.generic import TemplateView
from datetime import datetime
from eventos.models import Evento



class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos_proximos'] = Evento.objects.filter(data__gte=datetime.now()).order_by('data')
        context['show_proximos_eventos'] = True
        return context


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('eventos/', include('eventos.urls')),
    path('artistas/', include('artistas.urls')),
    path('', HomeView.as_view(), name='home'), 
]
