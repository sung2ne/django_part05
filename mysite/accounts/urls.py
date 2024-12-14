from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('register/', views.accounts_register, name='register'),
    path('login/', views.accounts_login, name='login'),
    path('logout/', views.accounts_logout, name='logout'),
    path('profile/', views.accounts_profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update_password/', views.update_password, name='update_password'),
    path('find_username/', views.find_username, name='find_username'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('withdraw/', views.accounts_withdraw, name='withdraw'),
]
