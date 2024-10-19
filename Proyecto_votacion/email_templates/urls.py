from django.urls import path
from email_templates import views

urlpatterns = [
   
    path('basic_action_email',views.BasicActionEmailView.as_view(),name='email_templates-basic_action_email'),
    path('alert_email',views.AlertEmailView.as_view(),name='email_templates-alert_email'),
    path('billing_email',views.BillingEmailView.as_view(),name='email_templates-billing_email'),


]