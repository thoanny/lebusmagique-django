from django.db import models


class Item(models.Model):
    RARITY_CHOICES = {
        "Junk": "Junk",
        "Basic": "Basic",
        "Fine": "Fine",
        "Masterwork": "Masterwork",
        "Rare": "Rare",
        "Exotic": "Exotic",
        "Ascended": "Ascended",
        "Legendary": "Legendary",
    }

    api_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    rarity = models.CharField(max_length=10, choices=RARITY_CHOICES, blank=True)
    icon = models.URLField(blank=True)
    data = models.JSONField(blank=True)

    def natural_key(self):
        return {
            "id": self.api_id,
            "name": self.name,
            "rarity": self.rarity,
            "icon": self.icon
        }