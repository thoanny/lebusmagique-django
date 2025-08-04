from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Decoration
import requests

@receiver(pre_save, sender=Decoration)
def set_decoration_from_api(sender, instance, **kwargs):
    response = requests.get(f"https://api.guildwars2.com/v2/guild/upgrades/{instance.upgrade_id}?lang=fr")
    if response.status_code == 200:
        data = response.json()
        instance.name = data.get('name')
        instance.icon = data.get('icon')