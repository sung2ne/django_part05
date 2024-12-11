from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.posts_create, name='create'),
    path('read/<int:post_id>/', views.posts_read, name='read'),
    path('update/<int:post_id>/', views.posts_update, name='update'),
    path('delete/<int:post_id>/', views.posts_delete, name='delete'),
    path('', views.posts_list, name='list'),
]