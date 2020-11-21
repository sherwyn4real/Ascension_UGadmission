from django.shortcuts import render
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

# Create your views here.
def login(request):
    return render(request,'college/login.html')

def signin_page(request):
    return render(request,'college/login2.html')

def signin(request):
    username = request.POST['uname']
    passw = request.POST['password']
    user = authenticate(request,username=username,password=passw)
    if user is not None:
        sign(request,user)
        return HttpResponseRedirect('/college/home/')
    else:
        return HttpResponse('Error Invalid Login')

@login_required
def home(request):
    logged_user = request.user
    username = logged_user.username
    college = userCollege.objects.get(username=username)
    info ={
        'college':college
    }
    return render(request,'college/choose-college.html',info)
    # get email, password
    # if mathches in data base
        # get all info from DB
        # return homepage, pass DB
    # else
        # return login page with message(invalid credentials)
    #return render(request,'college/home.html')

@login_required
def details(request):
    if(request.method=='POST'):
        return None

