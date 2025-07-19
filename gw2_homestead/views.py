from django.http import HttpResponse
from django.core import serializers
from .models import Cat, Node

def cat_list(request):
    query = Cat.objects.all()
    data = serializers.serialize('json', query, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')

def node_list(request):
    query = Node.objects.all()
    data = serializers.serialize('json', query, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')