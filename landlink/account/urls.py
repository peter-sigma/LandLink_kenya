from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.custom_signup_view, name='signup'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    
    
    path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('lawyer/dashboard/', views.lawyer_dashboard, name='lawyer_dashboard'),
]