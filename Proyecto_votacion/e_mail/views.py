from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class InboxView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Inbox"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Email"
        return render (request,'email/email-inbox.html',greeting)

class EmailReadView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Email Read"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Email"
        return render (request,'email/email-emailread.html',greeting)          

class EmailComposeView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Email Compose"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Email"
        return render (request,'email/email-emailcompose.html',greeting)          