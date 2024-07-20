from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    return render(request, 'base.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', home, name='home'),
    path('', include('eventos.urls')),
    path('', include('artistas.urls'))
]
