from django.urls import path
from . import views

urlpatterns = [
    path('artistas/list/', views.ArtistaListView.as_view(), name='artista_list'),
    path('artistas/create/', views.ArtistaCreateView.as_view(), name='artista_create'),
    path('artistas/<int:pk>/detail/', views.ArtistaDetailView.as_view(), name='artista_detail'),
    path('artistas/<int:pk>/update/', views.ArtistaUpdateView.as_view(), name='artista_update'),
    path('artistas/<int:pk>/delete/', views.ArtistaDeleteView.as_view(), name='artista_delete'),
]
