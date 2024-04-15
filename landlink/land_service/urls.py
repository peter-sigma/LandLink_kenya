# urls.py
from django.urls import path
from . import views

#app_name = 'land_service'

urlpatterns = [
    path('lawyer/select_service/', views.select_service, name='select_service'),
    path('lawyer/add_service/', views.add_service, name='add_service'),
    path('lawyer/services/', views.lawyer_services, name='lawyer_services'),
    path('lawyer/services/update/<int:service_id>/', views.update_service, name='update_service'),
]