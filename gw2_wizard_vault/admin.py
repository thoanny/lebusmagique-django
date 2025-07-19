from django.contrib import admin
from .models import Objective


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ["api_id", "title", "has_tip"]
    search_fields = ["api_id", "title"]


admin.site.register(Objective, ObjectiveAdmin)