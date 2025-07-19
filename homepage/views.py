import json
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    query = {
        'admin': '/admin',
        'gw2': {
            'homestead': {
                'cats': reverse('gw2_homestead:cat_list'),
                'nodes': reverse('gw2_homestead:node_list')
            },
            'wizard_vault': {
                'objectives': reverse('gw2_wizard_vault:objective_list')
            }
        },
    }
    return HttpResponse(json.dumps(query), content_type='application/json')

