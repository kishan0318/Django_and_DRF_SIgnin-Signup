from django.shortcuts import render

# Create your views here.
# from tkinter.tix import Tree
from .models import *

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
# from .models import Appointment, Department, Contact,Beds
from django.views.generic import ListView,View,CreateView,DetailView,DeleteView,TemplateView
from django.contrib.auth import authenticate, login,logout
from .forms import Logform,Register, Resetform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse_lazy,reverse

def home(request):
    return render(request,"authentication/index.html")

class ActiveLogin(View):
    def get(self, request):
        f=Logform(None)
        k={'data':f}
        return render(request,'authentication/login.html',k)
    def post(self,request):
        f=Logform(request.POST)
        k={'data':f}
        if f.is_valid():
            u=f.cleaned_data.get('username')
            p=f.cleaned_data.get('password')
            ur=authenticate(username=u,password=p)
            nxt=request.GET.get('next')
            if ur:
                login(request,ur)
                if nxt:
                    return redirect(nxt)
                else:
                    # return HttpResponse('Welcome Atul Mishra')
                    return render(request,'authentication/afterLogin.html')
        return render(request,'authentication/login.html',k)

class Signup(View): 
    def get(self,request):
        f=Register(None)
        return render(request,'authentication/signup.html',{"data":f})
    def post(self,request):
        f=Register(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get('password') 
            data.set_password(p)
            data.save()
            return redirect('login')
        return render(request,'authentication/signup.html',{"data":f})

# def reset_password(request):
#     if request.method=="GET":
#         return render(request,'authentication/reset.html')
#     if request.method=="POST":
#         if request.user.check_password(request.POST.get('previous_password')):
#             x=User.objects.filter(username=request.user.username)
#             x.set_password=request.POST.get('new_password')
#             x.save()
#             return HttpResponse('Password updated successfully')
#         # return HttpResponse('Something went wrong')
#     return HttpResponse('something went wrong')

# class Reset(View):
#     def get(self,request):
#         f=Resetform(None)
#         return render(request,"authentication/reset.html",{'data':f})
#     def post(self,request):
#         f=Resetform(request.POST)
#         if f.is_valid():
#             x=f.cleaned_data.get('old_password')
#             ur=authenticate(username=request.user.username,password=x)
#             x1=User.objects.get(username=request.user.username)
#             x1.set_password=f.cleaned_data.get('new_password')
#             x1.save()
#             return HttpResponse('password changed successfullyyy')
#         return HttpResponse('somthing wrong')

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            form = PasswordChangeForm(request.user)
            messages.error(request, 'Please correct the error below.')
            return render(request,'authentication/reset.html',{'form':form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authentication/reset.html', {
        'form': form
    })


def afterLog(request):
    return render (request,'authentication/afterLogin.html') 

        