from django.utils.html import format_html
from django.contrib import admin
from .models import Cat, NodeCost, NodeSource, Node
from .forms import CatForm, NodeForm


class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_id', 'food', 'thumbnail']
    search_fields = ['api_id', 'name']
    autocomplete_fields = ['food']
    ordering = ('name',)
    form = CatForm

    def thumbnail(self, obj):
        if obj.icon:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.icon, obj.icon)
        elif obj.food:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.food.icon, obj.food.icon)
        return "Ø"
    thumbnail.short_description = "Image"


class NodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'api_id', 'item', 'thumbnail']
    filter_horizontal = ('sources', 'costs',)
    autocomplete_fields = ['item']
    ordering = ('name',)
    form = NodeForm

    def thumbnail(self, obj):
        if obj.item:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.item.icon, obj.item.icon)
        return "Ø"
    thumbnail.short_description = "Image"


class NodeCostAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class NodeSourceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(Cat, CatAdmin)
admin.site.register(NodeCost, NodeCostAdmin)
admin.site.register(NodeSource, NodeSourceAdmin)
admin.site.register(Node, NodeAdmin)