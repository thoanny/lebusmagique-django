from django.utils.html import format_html
from django.contrib import admin
from .models import Decoration
from .forms import DecorationForm


class DecorationAdmin(admin.ModelAdmin):
    list_display = ['name', 'upgrade_id', 'thumbnail']
    search_fields = ['upgrade_id', 'name']
    ordering = ('name',)
    autocomplete_fields = ['item', 'media']
    form = DecorationForm

    def thumbnail(self, obj):
        if obj.media:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.media.file.url, obj.media.file.url)
        return "Ø"
    thumbnail.short_description = "Media"


admin.site.register(Decoration, DecorationAdmin)