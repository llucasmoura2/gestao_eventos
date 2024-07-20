from django.urls import path
from . import views

urlpatterns = [
    path('artistas/list/', views.ArtistaListView.as_view(), name='artista_list'),
    path('artistas/create/', views.ArtistaCreateView.as_view(), name='artista_create'),
    path('artista/<int:pk>/detail/', views.ArtistaDetailView.as_view(), name='artista_detail'),
]
