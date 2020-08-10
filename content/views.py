from django.shortcuts import render

# Create your views here.

def quizz(request):
    return render(request, "quiz.html")

