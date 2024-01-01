from django.urls import path
from . import views

urlpatterns = [
    path('handle-selected-date/', views.handle_selected_date, name='handle_selected_date'),
    path('', views.index, name='booktrip'),
]