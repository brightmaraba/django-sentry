# djsentry/errors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.errors_index, name="index"),
]
