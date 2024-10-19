from django.urls import path
from e_mail import views

urlpatterns = [
    #email
    path('inbox',views.InboxView.as_view(),name='email-inbox'),
    path('emailread',views.EmailReadView.as_view(),name='email-emailread'),
    path('emailcompose',views.EmailComposeView.as_view(),name='email-emailcompose'),

]