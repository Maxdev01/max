from django.shortcuts import render, redirect, reverse
from account.forms import RegisterForm
from course.models import Courses
from django.contrib import messages
from contact.forms import ContactForm

def home(request):
    #courses = Courses.objects.all()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        contactform = ContactForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Votre compte a ete cree avec succes')
        else:
            messages.error(request, 'Verifier vos informations')
    else:
        form = RegisterForm()
        contactform = ContactForm()
    return render(request, 'home.html', locals())
