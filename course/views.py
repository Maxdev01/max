from django.shortcuts import render, redirect, reverse
from account.forms import RegisterForm
from course.models import Courses, Pin, Students
from django.contrib import messages
from contact.forms import ContactForm

def home(request):
    courses = Courses.objects.all()
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

def cours(request):
    cours = Courses.objects.all()
    student = Students.objects.get(user=request.user)
    return render(request, "nos-cours.html", {'cours': cours})

def activatePIN(request, id=None):
    if request.method == 'POST':
        myPIN = request.POST.get('PIN')
        if myPIN:
            pin = Pin.objects.get(pin=myPIN)
            if pin and pin.used is not True:
                cours = Courses.objects.get(id=id)
                cours.active = True
                pin.used = True
                cours.save()
                student = Students.objects.get(user=request.user)
                student.course.add(cours)
                student.save()
                pin.save()
            else:
                messages.error(request, 'Pin invalide')
            return redirect('nos-cours')
            # else:
            #     #template
            #     pass
    return render(request, 'pin.html', {})
