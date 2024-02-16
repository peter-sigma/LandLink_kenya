# messaging/urls.py

from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('send/<int:receiver_id>/', views.send_message, name='send_message'),
    path('view/', views.view_messages, name='view_messages'),
    # Define URL patterns for messaging views
    # For example:
    # path('inbox/', views.inbox, name='inbox'),
    # path('compose/', views.compose, name='compose'),
    # path('message/<int:message_id>/', views.message_detail, name='message_detail'),
]

