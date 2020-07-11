from django.shortcuts import render, redirect
from account.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from course.views import home
from django.contrib import messages
# Create your views here.


def user_login(request):
   if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
         data = form.cleaned_data
         user = authenticate(request, username=data['username'], password=data['password'])
         if user is not None:
            if user.is_active:
               login(request, user)
               return  redirect(dashboard)
         messages.error(request, 'Veuiller verifier vos informations')
   else:
      form = LoginForm()
   return render(request, 'registration/login.html', {'form': form})


@login_required
def dashboard(request):
   return render(request, 'dashboard.html', {})


def user_logout(request):
   logout(request)
   return redirect('login')


def register(request):
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['password'])
         user.save()
         return redirect(user_login)
      messages.error(request, 'formulaire non valid')

   else:
      form = RegisterForm()
   return render(request, 'registration/register.html', {'form': form})     