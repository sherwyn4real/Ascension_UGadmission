from django.db import models
from django.forms import ModelForm

class Data(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address = models.TextField()
    phone = models.CharField(max_length=12)
    phy=models.IntegerField()
    chem = models.IntegerField()
    mathORbio = models.IntegerField()
    gcetphy = models.IntegerField()
    gcetchem = models.IntegerField()
    gcetmath = models.IntegerField()
    rankpm = models.IntegerField()
    neetphy = models.IntegerField()
    neetchem = models.IntegerField()
    neetbio = models.IntegerField()
    neetrank = models.IntegerField()
    FILE = models.FileField(upload_to = 'student_files')
    chosen_college = models.CharField(max_length=30)
    chosen_course = models.CharField(max_length=20)
    
    def put(self):
        return self.first_name

# Create your models here.
