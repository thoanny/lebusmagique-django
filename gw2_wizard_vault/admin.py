from django.contrib import admin
from .models import Objective


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ["title", "api_id", "has_tip"]
    search_fields = ["api_id", "title"]


admin.site.register(Objective, ObjectiveAdmin)