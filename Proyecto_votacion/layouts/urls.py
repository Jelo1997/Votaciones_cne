from django.urls import path
from layouts import views

urlpatterns = [
    # Vertical Layout
    path('light-Sidebar',views.LightSidebarView.as_view(),name='layouts-light_sidebar'),
    path('compact-Sidebar',views.CompactSidebarView.as_view(),name='layouts-compact_sidebar'),
    path('icon-Sidebar',views.IconSidebarView.as_view(),name='layouts-icon_sidebar'),
    path('boxed-width',views.BoxLayoutView.as_view(),name='layouts-boxed-width'),
    path('colored-Sidebar',views.ColoredSidebarView.as_view(),name='layouts-colored_sidebar'),

    #Horizontal Layout
    path('horizontal',views.HorizontalView.as_view(),name='layouts-horizontal'),
    path('horizontal-topbar-light',views.TopbarLightHoriView.as_view(),name='layouts-hori_topbar_light'),
    path('horizontal-boxed-width',views.BoxedWidthHoriView.as_view(),name='layouts-hori_boxed_width'),
    

]    