from django.contrib import admin
from .models import Course, userCollege
# Register your models here.
#admin.site.register(Course)
#admin.site.register(userCollege)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(userCollege)
class userCollegeAdmin(admin.ModelAdmin):
    list_display = ('name','email')
