from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://unpkg.com/easymde/dist/easymde.min.css', 'admin/css/easymde.css',)
        }
        js = (
            'https://unpkg.com/easymde/dist/easymde.min.js',
            'admin/js/easymde-id_description.js',
        )
