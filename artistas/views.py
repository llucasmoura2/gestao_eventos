from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms


class ArtistaListView(ListView):
    model = models.Artista
    template_name = 'artistas_list.html'
    context_object_name = 'artistas'


class ArtistaCreateView(CreateView):
    model = models.Artista
    template_name = 'artista_create.html'
    form_class = forms.ArtistaForm
    success_url = reverse_lazy('home')

class ArtistaDetailView(DetailView):
    model = models.Artista
    template_name = 'artista_detail.html'
