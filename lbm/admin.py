from django.utils.html import format_html
from django.contrib import admin
from .models import Media

class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'thumbnail')
    list_filter = ('category',)
    search_fields = ['name']
    ordering = ('name',)

    def thumbnail(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.file.url, obj.file.url)
        return "Ø"
    thumbnail.short_description = "Image"


admin.site.register(Media, MediaAdmin)