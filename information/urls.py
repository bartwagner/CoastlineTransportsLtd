from django.urls import path
from . import views

urlpatterns = [
    path('termsconditions', views.termsconditions, name='termsconditions'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('faq', views.faq, name='faq'),
    path('safety', views.safety, name='safety'),
    path('schedules', views.schedules, name='schedules'),
    path('tickets', views.tickets, name='tickets'),
]