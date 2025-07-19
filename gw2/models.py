from django.db import models


class Item(models.Model):
    RARITY_CHOICES = [
        ('Junk', 'Inutile (gris)'),
        ('Basic', 'Basique (blanc)'),
        ('Fine', 'Raffiné (bleu)'),
        ('Masterwork', 'Chef-d\'œuvre (vert)'),
        ('Rare', 'Rare (jaune)'),
        ('Exotic', 'Exotique (orange)'),
        ('Ascended', 'Élevé (rose)'),
        ('Legendary', 'Légendaire (violet)')
    ]

    api_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    rarity = models.CharField(max_length=10, choices=RARITY_CHOICES, blank=True)
    icon = models.URLField(blank=True)
    data = models.JSONField(blank=True)

    class Meta:
        verbose_name = 'objet'
        verbose_name_plural = 'objets'

    def natural_key(self):
        return {
            "id": self.api_id,
            "name": self.name,
            "rarity": self.rarity,
            "icon": self.icon
        }

    def __str__(self):
        return self.name;