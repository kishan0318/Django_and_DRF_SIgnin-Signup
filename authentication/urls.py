from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
   path('',home,name='home'),
   path("signup",Signup.as_view(),name='register'),
    path("signin",ActiveLogin.as_view(),name='login'),
    # path("reset_password",reset_password,name="reset_password"),
     path("afterLog",afterLog,name="afterLog"),
    url(r'^password/$', change_password, name='change_password')
]
