from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('create/', views.board_create, name='create'),
    path('list/', views.board_list, name='list'),
    path('read/<int:board_id>/', views.board_read, name='read'),
    path('update/<int:board_id>/', views.board_update, name='update'),
    path('delete/<int:board_id>/', views.board_delete, name='delete'),
    path('download/<int:board_id>/', views.board_download, name='download'),
]