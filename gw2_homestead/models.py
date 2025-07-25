from django.db import models
from gw2.models import Item, Currency, Source


class Cat(models.Model):
    api_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    food = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    waypoint = models.CharField(max_length=200, blank=True)
    map_name = models.CharField(max_length=200, blank=True)
    guide = models.URLField(blank=True)
    description = models.TextField(blank=True)
    icon = models.URLField(blank=True)

    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'chats'


class NodeCost(models.Model):
    amount = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.currency:
            return(f"{self.amount} × {self.currency}")
        else:
            return(f"{self.amount} × ???")

    def natural_key(self):
        data = {
           "id": self.id,
           "amount": self.amount,
           "currency": None
        }

        if self.currency:
            data['currency'] =  {
                "api_id": self.currency.api_id,
                "name": self.currency.name,
                "icon": self.currency.icon,
            }

        return data


class NodeSource(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.source.name

    def natural_key(self):
        return {
            "id": self.id,
            "source": {
                "id": self.source.id,
                "name": self.source.name,
                "icon": self.source.icon,
            }
        }


class Node(models.Model):
    api_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    costs = models.ManyToManyField(NodeCost, blank=True)
    sources = models.ManyToManyField(NodeSource, blank=True)

    class Meta:
        verbose_name = 'zone de récoltes'
        verbose_name_plural = 'zones de récoltes'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return(f"__node_{self.api_id}__")

'''
class Glyph(models.Model):
    api_id (str)
    name
    pass


class Decoration(models.Model):
    pass

'''