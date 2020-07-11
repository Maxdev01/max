from django.urls import path
from contact import views


urlpatterns = [
    path('sent/admin/', views.send_to_admin, name='send_to_admin'),
    path('sent/email', views.send_to_email, name='send_to_email'),
]