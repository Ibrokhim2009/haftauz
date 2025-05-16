from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app1"
    def ready(self):
        from .signals import models_change_signal,news_change_signals