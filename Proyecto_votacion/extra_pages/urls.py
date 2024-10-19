from django.urls import path
from extra_pages import views
urlpatterns = [
    path('timeline',views.TimelineView.as_view(),name='extra_pages-timeline'),
    path('invoice',views.InvoiceView.as_view(),name='extra_pages-invoice'),
    path('directory',views.DirectoryView.as_view(),name='extra_pages-directory'),
    path('starterpage',views.StarterPageView.as_view(),name='extra_pages-starterpage'),
    path('404error',views.ErrorView.as_view(),name='extra_pages-404error'),
    path('500error',views.ErrorsView.as_view(),name='extra_pages-500error'),
    path('pricing',views.PricingView.as_view(),name='extra_pages-pricing'),
    path('gallery',views.GalleryView.as_view(),name='extra_pages-gallery'),
    path('maintenance',views.MaintenanceView.as_view(),name='extra_pages-maintenance'),
    path('comingsoon',views.ComingSoonView.as_view(),name='extra_pages-comingsoon'), 
    path('faqs',views.FaqsView.as_view(),name='extra_pages-faqs'), 
    path('profile',views.ProfileView.as_view(),name='extra_pages-profile'), 

]