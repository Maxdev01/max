from django.urls import path
from course import views

urlpatterns = [
    path("", views.home, name='home'),
]