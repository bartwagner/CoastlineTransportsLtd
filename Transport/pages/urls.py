from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('safety', views.safety, name='safety'),
    path('schedules', views.schedules, name='schedules'),
    path('fares', views.fares, name='fares'),
    path('faq', views.faq, name='faq'),
    path('busCharters', views.busCharters, name='busCharters'),
    path('boxByBus', views.boxByBus, name='boxByBus')
]