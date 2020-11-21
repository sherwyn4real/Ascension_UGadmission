from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    info = models.CharField(max_length=50,help_text='info about course')
    COURSE_TYPE = (
        ('e','Engineering'),
        ('m','Medical')
    )
    COURSE_NAME = (
        ('comp','Computer Engineering'),
        ('it','Information Technology'),
        ('mech','Mechanical Engineering'),
        ('etc','Electronic and Telecomunication'),
        ('mbbs','MBBS'),
        ('den','Bachelor Dental Science')
    )

    course_type = models.CharField(
        max_length=1,
        choices=COURSE_TYPE,
        blank=True,
        default='e'
    )
    course_name = models.CharField(
        max_length=5,
        choices=COURSE_NAME,
        blank=True,
        default=''
    )
    
    def getInfo(self):
        return self.info

    def __str__(self):
        return self.info

class userCollege(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.TextField()
    username = models.TextField()
    password = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    course = models.ManyToManyField(Course)

  #  def display_course(self):
   #     return ', '.join( cor.name for cor in self.course.all() )

    def __str__(self):
        return self.name

