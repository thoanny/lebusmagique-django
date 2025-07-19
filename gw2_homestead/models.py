from django.db import models
from gw2.models import Item

class Cat(models.Model):
    api_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    food = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    waypoint = models.CharField(max_length=200, blank=True)
    map_name = models.CharField(max_length=200, blank=True)
    guide = models.URLField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'chats'

'''
class Node(models.Model):
    api_id (str)
    name
    description
    price (relation: gw2.currency)
    source
    pass


class Glyph(models.Model):
    api_id (str)
    name
    pass


class Decoration(models.Model):
    pass

'''