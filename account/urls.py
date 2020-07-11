from django.urls import path
from account import views
urlpatterns = [
   path('login', views.user_login, name='login'),
   path('register', views.register, name='register'),
   path('dashboard', views.dashboard, name='dashboard'),
   path('logout', views.user_logout, name='logout'),
]