# messaging/urls.py

from django.urls import path
from . import views


app_name='messaging'
urlpatterns = [
     path('load_chat', views.load_chat, name='load_chat'),
     path('create_chat', views.create_chat, name='create_chat'),
     path('view/chats', views.view_chats, name='view_chats'),
     path('view/open_chat/<int:chat_id>', views.open_chat, name='open_chat'),
     path('view/delete_chat/<int:chat_id>', views.delete_chat, name='delete_chat'),
     path('view/delete_view_chat/<int:chat_id>', views.delete_view_chat, name='delete_view_chat'),
    # #path('send/<int:receiver_id>/', views.send_message, name='send_message'),
    # path('view/', views.view_messages, name='view_messages'),
    
    path('send_custom_message/<int:chat_id>', views.send_custom_message_get, name='send_custom_message_get'),
    path('send_custom_message/post/<int:chat_id>', views.send_custom_message_post, name='send_custom_message_post'),
    path('view/delete_message/<int:message_id>', views.delete_message, name='delete_message'),

    path('load_custom_reply_message/<int:chat_id>/<int:message_id>', views.load_custom_reply_message, name='load_custom_reply_message'),
    path('send_custom_reply_message/<int:chat_id>/<int:message_id>', views.send_custom_reply_message, name='send_custom_reply_message'),
    #path('send_custom_message/<int:receiver_id>/', views.send_custom_message_post, name='send_custom_message'),

    # Define URL patterns for messaging views
    # For example:
    # path('inbox/', views.inbox, name='inbox'),
    # path('compose/', views.compose, name='compose'),
    # path('message/<int:message_id>/', views.message_detail, name='message_detail'),
]

