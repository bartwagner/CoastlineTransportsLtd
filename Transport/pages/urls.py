from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.faq, name='faq'),
    path('safety', views.safety, name='safety'),
    path('shipping', views.shipping, name='shipping'),
    path('charterBus', views.charterBus, name='charterBus')
]