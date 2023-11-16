from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='register'),
    path('', views.registerCostumer, name='registerCostumer')
]