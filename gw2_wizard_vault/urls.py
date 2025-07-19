from django.urls import path
from .views import objective_list

urlpatterns = [
    path('objectives/', objective_list, name='objective_list'),
]