from django.urls import path

from . import views

app_name = "gw2"
urlpatterns = [
    path("", views.index, name="index"),
]