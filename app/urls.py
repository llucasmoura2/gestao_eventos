from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from accounts.views import login_view, logout_view, register_view


def home(request):
    return render(request, 'base.html')

urlpatterns = [
    path('admin/', admin.site.urls),


    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('', include('eventos.urls')),
    path('', include('artistas.urls'))
]
