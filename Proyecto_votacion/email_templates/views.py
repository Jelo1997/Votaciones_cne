from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class BasicActionEmailView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Basic Action Email"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Email Templates"
        return render (request,'email_templates/email_templates-basicactionemail.html',greeting)

class AlertEmailView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Alert Email"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Email Templates"
        return render (request,'email_templates/email_templates-alert_email.html',greeting)        

class BillingEmailView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Billing Email"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Email Templates"
        return render (request,'email_templates/email_templates-billing_email.html',greeting)         