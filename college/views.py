from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from college.models import Course,userCollege
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth import login as sign

class CourseListView(generic.ListView):
    model = Course

class CollegeListView(generic.ListView):
    model = userCollege

def signin_page(request):
    return render(request,'college/login2.html',context={})

def signin(request):
    username = request.POST['uname']
    passw = request.POST['password']
    user = authenticate(request,username=username,password=passw)
    if user is not None:
        sign(request,user)
        return redirect('college_home')
    else:
        message = {'form':True}
        return render(request,'college/login2.html',message)

@login_required(login_url='/college/log')
def home(request):
    logged_user = request.user
    if(logged_user.is_authenticated == True):
        usn = logged_user.username
        college = userCollege.objects.all().get(username=usn)
        info ={
            'college':college,
            'courses':college.course.all()
        }
        return render(request,'college/choose-course.html',info)
    else:
        return render(request,'college/login2.html')


@login_required(redirect_field_name='signin_page')
def details(request):
    if(request.method=='POST'):
        return None