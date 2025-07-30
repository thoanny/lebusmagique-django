from django import forms
from .models import Cat, Node


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://unpkg.com/easymde/dist/easymde.min.css', 'admin/css/easymde.css',)
        }
        js = (
            'https://unpkg.com/easymde/dist/easymde.min.js',
            'admin/js/easymde-id_description.js',
        )

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://unpkg.com/easymde/dist/easymde.min.css', 'admin/css/easymde.css',)
        }
        js = (
            'https://unpkg.com/easymde/dist/easymde.min.js',
            'admin/js/easymde-id_description.js',
        )