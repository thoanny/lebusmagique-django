from django.utils.html import format_html
from django.contrib import admin
from .models import Item, Currency, Source


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_id', 'rarity', 'thumbnail']
    search_fields = ['api_id', 'name']
    ordering = ('name',)

    def thumbnail(self, obj):
        if obj.icon:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.icon, obj.icon)
        return "Ø"
    thumbnail.short_description = "Icon"


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_id', 'thumbnail']
    search_fields = ['name']
    ordering = ('name',)

    def thumbnail(self, obj):
        if obj.icon:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.icon, obj.icon)
        return "Ø"
    thumbnail.short_description = "Icon"

class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail']
    search_fields = ['name']
    ordering = ('name',)

    def thumbnail(self, obj):
        if obj.icon:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.icon, obj.icon)
        return "Ø"
    thumbnail.short_description = "Icon"

admin.site.register(Item, ItemAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Source, SourceAdmin)