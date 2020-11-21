from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,Studentform
from django.contrib.auth.decorators import login_required
from college.models import *

def register(request):
    if request.method== 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created. You can now apply for admission')
            return redirect('admit')
        
    else:
         form = UserRegisterForm()
    return render(request, 'student/register.html', {'form': form })


def admit(request):
    if request.method == 'POST':
        form = Studentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f'Admission request successful. You will hear from us soon')
            return redirect('home')
        
    else:
        form = Studentform()
    return render(request,'student/admit.html', {'form': form})

@login_required
def courses(request):
    crs = Course.objects.all()
    info = {'courses': crs}

    return render(request, 'student/courses.html',context= info)

@login_required
def colleges(request, id):
    c = Course.objects.get(id=id)
    college = userCollege.objects.all()
    clg = college.filter(course=c)
    info = {'colleges': clg}

    return render(request, 'student/colleges.html', context=info )

    


