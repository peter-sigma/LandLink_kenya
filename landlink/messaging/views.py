# messaging/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.models import User
from .models import Message
from account.models import CustomUser

@login_required
def send_message(request, receiver_id):
    if request.method == 'POST':
        message_content = request.POST.get('message_content')
        receiver = CustomUser.objects.get(pk=receiver_id)
        sender = request.user
        Message.objects.create(sender=sender, receiver=receiver, content=message_content)
        messages.success(request, 'Message sent successfully!')
        return redirect('buyer_dashboard')  # Redirect to dashboard after sending message
    else:
        receiver = CustomUser.objects.get(pk=receiver_id)
        return render(request, 'messaging/send_message.html', {'receiver': receiver})

@login_required
def view_messages(request):
    user = request.user
    all_messages = Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)
    return render(request, 'messaging/view_messages.html', {'messages': all_messages})

