from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('land/<int:land_id>/', views.land_detail, name='land_detail'),
    path('add_land/', views.add_land, name='add_land'),
    path('lands/<int:land_id>/update-location/', views.update_location, name='update_location'),
    path('lands/update-location/', views.update_location_view, name='update_location_view'),
]