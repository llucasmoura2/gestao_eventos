from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from . import models, forms


class EventoListView(ListView):
    model = models.Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'


class EventoCreateView(CreateView):
    model = models.Evento
    template_name = 'evento_create.html'
    form_class = forms.EventoForm
    success_url = reverse_lazy('home')


class EventoDetailView(DetailView):
    model = models.Evento
    template_name = 'evento_detail.html'


class EventoUpdateView(UpdateView):
    model = models.Evento
    template_name = 'evento_update.html'
    form_class = forms.EventoForm
    success_url = reverse_lazy('evento_list')


class EventoDeleteView(DeleteView):
    model = models.Evento
    template_name = 'evento_delete.html'
    success_url = reverse_lazy('evento_list')
