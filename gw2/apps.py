from django.apps import AppConfig


class Gw2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gw2'
    verbose_name="[GW2] API"

    def ready(self):
        import gw2.signals