from django.urls import path
from .views import media_list

app_name = "lbm"
urlpatterns = [
    path('medias/', media_list, name='media_list'),
]