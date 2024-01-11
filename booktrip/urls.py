from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booktrip'),
    path('handle-selected-date-board/', views.handle_selected_date_board, name='handle_selected_date_board'),
    path('handle-selected-board-destination/', views.handle_selected_board_destination, name='handle_selected_board_destination'),
    path('handle-selected-local-board-destination/', views.handle_selected_local_board_destination, name='handle-selected-local-board-destination'),
]