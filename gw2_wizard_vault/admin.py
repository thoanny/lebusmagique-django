from django.contrib import admin
from .models import Objective
from .forms import ObjectiveForm


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ["title", "api_id", "has_tip"]
    search_fields = ["api_id", "title"]
    form = ObjectiveForm


admin.site.register(Objective, ObjectiveAdmin)