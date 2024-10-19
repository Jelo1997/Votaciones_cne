from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class loginView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "login"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/login.html',greeting)
    
class login2View(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "login2"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/login-2.html',greeting)
    
class RegisterView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "register"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/register.html',greeting)
    
class Register2View(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "register-2"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/register-2.html',greeting)
    
    
class RecoverpasswordView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "recover-password"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/recover-password.html',greeting)
    
  
class Recoverpassword2View(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "recover-password-2"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/recover-password-2.html',greeting)
    
class LockscreenView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "lock-screen"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/lock-screen.html',greeting)

class Lockscreen2View(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "lock-screen-2"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "authentication"
        return render (request,'authentication/lock-screen-2.html',greeting)