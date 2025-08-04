from django.db import models
from lbm.models import Media
from gw2.models import Item

'''
name (récupéré automatiquement avec upgrade_id)
recipe_id (récupéré automatiquement si item_id est renseigné, prendre le premier)
'''

class Decoration(models.Model):
    upgrade_id = models.PositiveIntegerField(unique=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_id = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, help_text="Renseigné automatiquement depuis l'API si upgrade id existant")
    icon = models.URLField(blank=True, help_text="Renseigné automatiquement depuis l'API si upgrade id existant")
    description = models.TextField(blank=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'décoration'
        verbose_name_plural = 'décorations'
