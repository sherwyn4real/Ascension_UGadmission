from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='college/login.html'),name='login_page'),
    path('log/',views.signin_page,name='signin_page'),
    path('loginfo/',views.signin,name='signin'),
    path('logout/',auth_views.LogoutView.as_view(template_name='college/logout.html'),name='logout_page'),
    path('home/',views.home,name='college_home')
]
