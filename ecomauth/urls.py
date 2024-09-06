from django.urls import path
from ecomauth import views

urlpatterns = [
    path('', views.index, name="index"),
]
