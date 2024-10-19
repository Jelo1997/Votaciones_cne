from django.urls import path
from authentication import views

urlpatterns = [
    path('login',views.loginView.as_view(),name='login'),
    path('login-2',views.login2View.as_view(),name='login-2'),
    path('register',views.RegisterView.as_view(),name='register'),
    path('register-2',views.Register2View.as_view(),name='register-2'),
    path('recover-password',views.RecoverpasswordView.as_view(),name='recover-password'),
    path('recover-password-2',views.Recoverpassword2View.as_view(),name='recover-password-2'),
    path('lock-screen',views.LockscreenView.as_view(),name='lock-screen'),
    path('lock-screen-2',views.Lockscreen2View.as_view(),name='lock-screen-2'),
  
]