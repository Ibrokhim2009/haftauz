from django.dispatch import receiver

from base.helper import send_mail
from .models import *
from django.db.models.signals import post_save
from .models import *

@receiver(post_save,sender=Category)
def models_change_signal(post_save,instance,created,**kwargs):
    print(f'\nInstance: {instance.title}\nCreated: {created}')



@receiver(post_save,sender=New)
def news_change_signals(sender,instance,created,**kwargs):
    if created:
        for i in Sub.objects.filter(is_sib=True):
            send_mail(title='Saytda yangi yangilik qoshildi',message=f'{instance.title}, ')
    else:
        send_mail(title='Saytda malumot ozgartirildi', message=f'{instance.title}, ')

















