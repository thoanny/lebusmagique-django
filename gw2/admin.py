from django.contrib import admin
from .models import Item, Currency, Source


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "api_id", "rarity"]
    search_fields = ["api_id", "name"]
    ordering = ('name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["name", "api_id"]
    search_fields = ["name"]


admin.site.register(Item, ItemAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Source)