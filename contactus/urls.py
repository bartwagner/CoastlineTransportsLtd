from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contactus'),
    path('email', views.email, name='email')
]
