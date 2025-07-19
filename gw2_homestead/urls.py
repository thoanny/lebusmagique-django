from django.urls import path
from .views import cat_list, node_list

app_name = "gw2_homestead"
urlpatterns = [
    path('cats/', cat_list, name='cat_list'),
    path('nodes/', node_list, name='node_list'),
]