from django.contrib import admin
from . import models


@admin.register(models.Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'banco', 'tipo_chave_pix', 'chave_pix',)
    search_fields = ('nome', 'cpf', 'telefone',)

