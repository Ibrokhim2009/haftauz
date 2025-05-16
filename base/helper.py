

from django.conf import settings
from django.core.mail import send_mail


def send_mail(message,title,reciept):
    send_mail(subject=title,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[reciept]
                  )