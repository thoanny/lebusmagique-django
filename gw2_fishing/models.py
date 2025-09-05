from django.db import models
from gw2.models import Item
import locale
from datetime import date


class Achievement(models.Model):
    name = models.CharField(max_length=200)
    achievement_id = models.PositiveIntegerField(null=True, blank=True)
    repeat_achievement_id = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'succès'
        verbose_name_plural = 'succès'

    def __str__(self):
        return self.name

    def natural_key(self):
        return {
            "id": self.id,
            "name": self.name,
            "achievement_id": self.achievement_id,
            "repeat_achievement_id": self.repeat_achievement_id
        }


class Bait(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    power = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'appât'
        verbose_name_plural = 'appâts'

    def __str__(self):
        return self.item.name

    def natural_key(self):
        return {
            "id": self.id,
            "item": {
                "id": self.item.api_id,
                "name": self.item.name,
                "rarity": self.item.rarity,
                "icon": self.item.icon
            },
            "power": self.power
        }


class Hole(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'zone de pêche'
        verbose_name_plural = 'zones de pêche'

    def __str__(self):
        return self.name


class Fish(models.Model):
    SPECIALIZATIONS = [
        ('vindicator', 'Justicier'),
        ('mechanist', 'Méchamancien'),
        ('harbinger', 'Augure'),
        ('specter', 'Spectre'),
        ('willbender', 'Subjugueur'),
        ('bladesworn', 'Jurelame'),
        ('untamed', 'Indomptable'),
        ('virtuoso', 'Virtuose'),
        ('catalyst', 'Catalyseur'),
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    power_min = models.PositiveIntegerField(null=True, blank=True)
    power_max = models.PositiveIntegerField(null=True, blank=True)
    bait = models.ForeignKey(Bait, on_delete=models.SET_NULL, null=True, blank=True)
    bait_any = models.BooleanField()
    achievement = models.ForeignKey(Achievement, on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.CharField(max_length=10, choices=SPECIALIZATIONS, null=True, blank=True)
    strange_diet_achievement = models.BooleanField()
    daily_catch = models.BooleanField()

    class Meta:
        verbose_name = 'poisson'
        verbose_name_plural = 'poissons'

    def __str__(self):
        return self.item.name




class FishHole(models.Model):
    FREQUENCIES = [
        ('low', 'Faible chance'),
        ('best', 'Meilleure chance'),
        ('high', 'Fréquemment repéré'),
    ]
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=5, choices=FREQUENCIES, null=True, blank=True)

    class Meta:
        verbose_name = 'zone de pêche'
        verbose_name_plural = 'zones de pêche'

class Time(models.Model):
    MOMENTS = [
        ('tyria_dusk_dawn', 'Aube/Crépuscule [Tyrie centrale]'),
        ('tyria_day', 'Jour [Tyrie centrale]'),
        ('tyria_night', 'Nuit [Tyrie centrale]'),
        ('cantha_dusk_dawn', 'Aube/Crépuscule [Cantha]'),
        ('cantha_day', 'Jour [Cantha]'),
        ('cantha_night', 'Nuit [Cantha]'),
        ('any', 'Quelconque'),
    ]
    FREQUENCIES = [
        ('low', 'Faible chance'),
        ('best', 'Meilleure chance'),
    ]
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    moment = models.CharField(max_length=20, choices=MOMENTS)
    frequency = models.CharField(max_length=5, choices=FREQUENCIES, null=True, blank=True)

    class Meta:
        verbose_name = 'horaire'
        verbose_name_plural = 'horaires'


class Daily(models.Model):
    date = models.DateField(unique=True)
    arborstone = models.ForeignKey(Fish, on_delete=models.CASCADE, verbose_name='Pierre Arborea', related_name='arborstone', blank=True, null=True)
    lowland_shore = models.ForeignKey(Fish, on_delete=models.CASCADE, verbose_name='Côte des basses terres', related_name='lowland_shore', blank=True, null=True)
    janthir_syntri = models.ForeignKey(Fish, on_delete=models.CASCADE, verbose_name='Syntri de Janthir', related_name='janthir_syntri', blank=True, null=True)
    mistburned_barrens = models.ForeignKey(Fish, on_delete=models.CASCADE, verbose_name='Landes de Feu-de-Brume', related_name='mistburned_barrens', blank=True, null=True)

    class Meta:
        verbose_name = 'quotidiens'
        verbose_name_plural = 'quotidiens'

    def __str__(self):
        locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
        return self.date.strftime('%d %B %Y')