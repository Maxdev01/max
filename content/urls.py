from django.urls import path
from content import views 
urlpatterns = [
     path('quizz', views.quizz, name="Quizz")
]