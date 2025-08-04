from django.apps import AppConfig


class Gw2GuildConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gw2_guild'
    verbose_name="[GW2] Guildes"

    def ready(self):
        import gw2_guild.signals