from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ArtistaListView(ListView):
    model = models.Artista
    template_name = 'artistas_list.html'
    context_object_name = 'artistas'


@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class ArtistaCreateView(CreateView):
    model = models.Artista
    template_name = 'artista_create.html'
    form_class = forms.ArtistaForm
    success_url = reverse_lazy('home')

class ArtistaDetailView(DetailView):
    model = models.Artista
    template_name = 'artista_detail.html'


@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class ArtistaUpdateView(UpdateView):
    model = models.Artista
    template_name = 'artista_update.html'
    form_class = forms.ArtistaForm
    success_url = reverse_lazy('artista_list')

@method_decorator(login_required (login_url='login'), name='dispatch')
class ArtistaDeleteView(DeleteView):
    model = models.Artista
    template_name = 'artista_delete.html'
    success_url = reverse_lazy('artista_list')
