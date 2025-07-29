from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Item
import requests

@receiver(pre_save, sender=Item)
def set_item_from_api(sender, instance, **kwargs):
    response = requests.get(f"https://api.guildwars2.com/v2/items/{instance.api_id}?lang=fr")
    if response.status_code == 200:
        data = response.json()
        instance.name = data.get('name')
        instance.rarity = data.get('rarity')
        instance.icon = data.get('icon')
        instance.data = data