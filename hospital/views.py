from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from .models import *


# Create your views here.

def home(request):
    # return  HttpResponse ('hello world')
    if not request.user.is_staff:
        return redirect('login')
    return render (request,'index.html')


def about(request):
  return render(request,'about.html')

def contact(request):
  return render(request,'contact.html')

def blog(request):
  return render(request,'blog.html')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc =  Doctor.objects.all()
    d ={ 'doc': doc}
    return render (request,'view_doctor.html', d)



def add_doctor(request):
    error=" "
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
      n = request.POST['name']
      c = request.POST['contact']
      sp = request.POST['special']

    #   user =authenticate(name=n, contact=c , special=sp)
      try:
         Doctor.objects.create(name=n,mobile=c,special=sp)
         error="no"
      except:
            error ="yes"

    d ={'error':error}
    return render (request,'add_doctor.html',d)

def login(request):
    error=" "
    if request.method =='POST':
      u = request.POST['username']
      p = request.POST['password']
      user =authenticate(username=u, password=p)
      try:
          if user.is_staff:
              login(request,user)
              error="no"
          else:
                  error ="yes"

      except:
            error ="yes"

    d ={'error':error}
    return render (request,'login.html',d)
          

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def delete_doctor(request,pid):
     if not request.user.is_staff:
        return redirect('login')

     doctor = Doctor.objects.get(id=pid)
     doctor.delete()
     return redirect('view_doctor')
