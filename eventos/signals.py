from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Evento)
def pos_save_evento(sender, instance, **kwargs):
    print('Evento criado')
    print(instance)
