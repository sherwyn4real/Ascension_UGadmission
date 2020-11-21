from django.shortcuts import render


def home(request):
    return render(request, 'UGapp/home.html')


# Create your views here.
