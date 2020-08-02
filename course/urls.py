from django.urls import path
from course import views

urlpatterns = [
    path("", views.home, name='home'),
    path('nos-cours/', views.cours, name="nos-cours"),
    path('activation/<str:id>/', views.activatePIN, name='pin'),

]