from django.urls import path
from .views import fish_list, daily_list

app_name = "gw2_fishing"
urlpatterns = [
    path('fishes/', fish_list, name='fish_list'),
    path('daily/', daily_list, name='daily_list'),
]