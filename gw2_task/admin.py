from django.contrib import admin
from .models import Task
from .forms import TaskForm


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'uid', 'period', 'start_date', 'end_date']
    search_fields = ['title', 'uid']
    form = TaskForm

admin.site.register(Task, TaskAdmin)