from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.posts_create, name='create'),
    path('<int:post_id>/', views.posts_read, name='read'),
    path('<int:post_id>/update/', views.posts_update, name='update'),
    path('<int:post_id>/delete/', views.posts_delete, name='delete'),
    path('', views.posts_list, name='list'),
    path('<int:post_id>/download/', views.posts_download, name='download'),
]