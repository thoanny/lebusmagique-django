from django.http import HttpResponse
from django.core import serializers
from .models import Objective

def objective_list(request):
    query = Objective.objects.all()
    data = serializers.serialize('json', query, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')

