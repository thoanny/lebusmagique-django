from django.http import HttpResponse
from django.core import serializers
from .models import Task

def task_list(request):
    query = Task.objects.all()
    data = serializers.serialize('json', query, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')