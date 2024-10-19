from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TimelineView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Timeline"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-timeline.html',greeting)    

class InvoiceView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Invoice"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-invoice.html',greeting)     

class DirectoryView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Directory"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-directory.html',greeting)   

class StarterPageView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Starter Page"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-starterpage.html',greeting)  

class ErrorView(LoginRequiredMixin,View):
    def get(self, request):
        return render (request,'extra_pages/extra_pages-404error.html')  

class ErrorsView(LoginRequiredMixin,View):
    def get(self, request):
        return render (request,'extra_pages/extra_pages-500error.html')                                      

class PricingView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Pricing"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-pricing.html',greeting)  

class GalleryView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Gallery"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-gallery.html',greeting) 

class MaintenanceView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Maintenance"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-maintenance.html',greeting)   

class ComingSoonView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Coming Soon"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-comingsoon.html',greeting)                  


class FaqsView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "FAQs"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-faqs.html',greeting)    
    


class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Profile"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-profile.html',greeting)           