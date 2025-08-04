from django.urls import path
from .views import decoration_list

app_name = "gw2_guild"
urlpatterns = [
    path('decorations/', decoration_list, name='decoration_list'),
]