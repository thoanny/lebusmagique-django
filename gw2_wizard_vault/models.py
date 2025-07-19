from django.contrib import admin
from django.db import models

class Objective(models.Model):
    api_id = models.PositiveIntegerField(unique=True, blank=False, verbose_name="ID API")
    title = models.CharField(max_length=200, blank=True, verbose_name="Titre")
    tip = models.TextField(blank=True, verbose_name="Conseil")

    class Meta:
        verbose_name = 'Objectif'
        verbose_name_plural = 'Objectifs'

    @admin.display(
        boolean=True,
        description="Conseil",
    )
    def has_tip(self):
            return self.tip != ""