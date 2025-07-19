from django.contrib import admin
from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = ["name", "api_id", "food"]
    search_fields = ["api_id", "name"]


admin.site.register(Cat, CatAdmin)