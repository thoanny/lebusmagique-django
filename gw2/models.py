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
    data = models.JSONField(blank=True, default=dict)

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
        if self.name:
            return self.name
        else:
            return(f"__item_{self.api_id}__")


class Currency(models.Model):
    api_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    icon = models.URLField(blank=True)
    data = models.JSONField(blank=True, default=dict)

    class Meta:
        verbose_name = 'monnaie'
        verbose_name_plural = 'monnaies'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return(f"__currency_{self.api_id}__")


class Source(models.Model):
    icon = models.URLField(blank=True)
    name = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'source'
        verbose_name_plural = 'sources'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return(f"__source_{self.id}__")