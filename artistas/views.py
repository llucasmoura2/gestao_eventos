from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
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
    success_url = reverse_lazy('artista_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
    def form_invalid(self, form):  
        messages.error(self.request, 'Erro ao criar artista. Verifique os dados e tente novamente.')
        return self.render_to_response(self.get_context_data(form=form))
    


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
