from django.urls import path
from .views import objective_list

app_name = "gw2_wizard_vault"
urlpatterns = [
    path('objectives/', objective_list, name='objective_list'),
]