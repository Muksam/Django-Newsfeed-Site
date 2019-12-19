from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
  content = {
    'title': 'home',
    'sliderData': Slider.objects.all()

}
  return render(request, 'pages/home.html', content)

def about(request):
  content = {
    'title' : 'about'
  }
  return render(request, 'pages/about.html', content)

def contact(request):
  content= {
     'title' : 'contact'
  }
  return render(request, 'pages/contact.html',content)

def news_details(request,slug):
  content = {
    'newsDetailsData' : News.objects.filter(slug=slug)
  }
  return render(request, 'pages/news-details.html',content)

def slider_details(request,slug):
    content = {
        'sliderDetailsData': Slider.objects.filter(slug=slug)
    }
    return render(request, 'pages/slider-details.html',content)



def user_login(request):
  if request.method == 'POST':
      data = AuthenticationForm(data=request.POST)
      if data.is_valid():
          user = data.get_user()
          login(request,user)
          return redirect('users')
      else:
          return redirect('login')
  else:
    content = {
    'loginForm': AuthenticationForm
  }
  return render(request,'pages/accounts/login.html',content)

def register(request):
    if request.method == 'POST':
        data = UserCreationForm(request.POST)
        if data.is_valid():
           data.save()
           messages.success(request, 'User was successfully register')
           return redirect('register')
        else:
           return redirect('register')
    else:
        content ={
        'userRegister': UserCreationForm
        }
        return render(request,'pages/accounts/register.html',content)

@login_required(login_url='login')
def users(request):
  content = {
    'title' : 'User'
  }
  return render(request, 'pages/user.html', content)


def user_logout(request):
     if request.method == 'POST':
         logout(request)
         return redirect('login')
     else:
         return HttpResponse('Invalid Access')



