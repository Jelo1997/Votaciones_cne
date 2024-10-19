from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

#########Vertical View#################
class LightSidebarView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Light Sidebar"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-light_sidebar.html',greeting)

class CompactSidebarView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Compact Sidebar"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-compact_sidebar.html',greeting) 

class IconSidebarView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Icon Sidebar"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-icon_sidebar.html',greeting)        

class BoxLayoutView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Boxed Layout"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-boxlayout.html',greeting)  

class ColoredSidebarView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Colored Sidebar"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-coloredsidebar.html',greeting)  

####Horizontal View#########
class HorizontalView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Horizontal"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-horizontal.html',greeting)  

class TopbarLightHoriView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Light Topbar"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-topbarlighthori.html',greeting)    

class BoxedWidthHoriView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Boxed Layout"
        greeting['heading'] = "holamundo"
        greeting['subheading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-boxwidthhori.html',greeting)                                          