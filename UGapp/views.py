from django.shortcuts import render


def home(request):
    logged_user = request.user
    usn = logged_user.username
    
    return render(request, 'UGapp/home.html')


# Create your views here.
