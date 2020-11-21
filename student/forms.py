from django import forms
from .models import Data
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

class Studentform(forms.ModelForm):
    class Meta:
        model=Data
        fields = ['first_name','middle_name','last_name','address', 'phone', 'phy',
                  'chem', 'mathORbio', 'gcetphy', 'gcetchem','gcetmath', 'rankpm', 'neetphy',
                  'neetchem', 'neetbio', 'neetrank','FILE',]
        
