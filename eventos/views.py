from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class EventoListView(ListView):
    model = models.Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'
    paginate_by = 6


@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class EventoCreateView(CreateView):
    model = models.Evento
    template_name = 'evento_create.html'
    form_class = forms.EventoForm
    success_url = reverse_lazy('home')


class EventoDetailView(DetailView):
    model = models.Evento
    template_name = 'evento_detail.html'


@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class EventoUpdateView(UpdateView):
    model = models.Evento
    template_name = 'evento_update.html'
    form_class = forms.EventoForm
    success_url = reverse_lazy('evento_list')


@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class EventoDeleteView(DeleteView):
    model = models.Evento
    template_name = 'evento_delete.html'
    success_url = reverse_lazy('evento_list')
