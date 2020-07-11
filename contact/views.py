from django.shortcuts import render, redirect
from django.http import HttpResponse
from contact.models import ContactModel
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.conf import settings
from django.core.mail import send_mail
# Create your views here

@require_POST
def send_to_admin(request):
    data = request.POST
    ContactModel(nom=data['nom'], email=data['email'], message=data['message']).save()
    print(request.POST)
    messages.success(request, 'message has been sent')
    return redirect('home')

@require_POST
def send_to_email(request):
    msg = request.POST.get('message')
    return HttpResponse('sent')
    


