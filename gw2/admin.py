from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "api_id", "rarity"]
    search_fields = ["api_id", "name"]


admin.site.register(Item, ItemAdmin)