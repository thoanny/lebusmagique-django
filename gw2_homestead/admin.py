from django.contrib import admin
from .models import Cat, NodeCost, NodeSource, Node


class CatAdmin(admin.ModelAdmin):
    list_display = ["name", "api_id", "food"]
    search_fields = ["api_id", "name"]


class NodeAdmin(admin.ModelAdmin):
    filter_horizontal = ('sources', 'costs',)


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