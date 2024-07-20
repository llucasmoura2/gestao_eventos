from django.urls import path
from . import views

urlpatterns = [
    path('eventos/list/', views.EventoListView.as_view(), name='evento_list'),
    path('eventos/create/', views.EventoCreateView.as_view(), name='evento_create'),
    path('eventos/<int:pk>/detail/', views.EventoDetailView.as_view(), name='evento_detail'),
    path('eventos/<int:pk>/update/', views.EventoUpdateView.as_view(), name='evento_update'),
    path('eventos/<int:pk>/delete/', views.EventoDeleteView.as_view(), name='evento_delete'),
]
