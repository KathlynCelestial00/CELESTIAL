from django.urls import path
from . import views

urlpatterns = [
    path('celestial', views.home, name='home'),
]