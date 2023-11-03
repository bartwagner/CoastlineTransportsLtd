from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('faq', views.faq, name='faq'),
    path('safety', views.safety, name='safety'),
    path('shipping', views.shipping, name='shipping'),
    path('charterBus', views.charterBus, name='charterBus'),
    path('tickets', views.tickets, name='tickets'),
    path('schedules', views.schedules, name='schedules'),
    path('bookTrip', views.bookTrip, name='bookTrip'),
    path('contactUs', views.contactUs, name='contactUs'),



    path('loyaltyRegister', views.loyaltyRegister, name='loyaltyRegister'),
    path('privacyPolicy', views.privacyPolicy, name='privacyPolicy'),
    path('termsConditions', views.termsConditions, name='termsConditions'),
    path('cancelChangesReserve', views.cancelChangesReserve, name='cancelChangesReserve')
]