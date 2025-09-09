from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'uid', 'period', 'start_date', 'end_date']
    search_fields = ['title', 'uid']

admin.site.register(Task, TaskAdmin)