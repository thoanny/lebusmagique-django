from django.urls import path
from .views import cat_list

app_name = "gw2_homestead"
urlpatterns = [
    path('cats/', cat_list, name='cat_list'),
]