# messaging/views.py
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.models import User
from .models import Message
from account.models import CustomUser
from .models import Chat


@login_required
def load_chat(request):
    current_user = request.user
    receivers = CustomUser.objects.exclude(pk=current_user.pk)   
    return render(request, 'messaging/load_chat.html', {'receivers': receivers})

        
        
        
@login_required
def create_chat(request):
    if request.method =='POST':
        receiver_id = request.POST.get('receiver_id')
        sender = request.user
        receiver = CustomUser.objects.get(pk=receiver_id)
        chat1 = Chat.objects.filter(sender=sender).filter(receiver=receiver)
        #check if the chat already exists and exit if it exists
        if not chat1.exists():
            #check if there is another chat created by the receiver
            chat2 = Chat.objects.filter(sender=receiver).filter(receiver=sender)
            if not chat2.exists():
                chat1.create(sender=sender, receiver=receiver)
                print("chat created")
                print(chat1)
                
            else:
                print("Two chats exists.... Danger!!!!!")
                
            
            
            
            return redirect('messaging:view_chats')
        else:
            print("chat already exists")
            return redirect('buyer_dashboard')
    

@login_required
def view_chats(request):
    # Get all chats related to the current user
    user_chats = Chat.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    
    return render(request, 'messaging/view_chats.html', {'user_chats': user_chats})

@login_required
def open_chat(request, chat_id):
    chat = Chat.objects.get(pk=chat_id)
    messages = Message.objects.filter(chat=chat_id)
    children = Message.objects.filter(chat=chat_id).exclude(parent=0)
   # Extract parent message IDs from the child messages
    parent_ids = children.values_list('parent', flat=True).distinct()
     # Retrieve parent messages using the extracted IDs
    parents = Message.objects.filter(id__in=parent_ids)
    no_of_replys=parents.count()
    return render(request, 'messaging/open_chat.html', {"messages": messages, "parents" : parents, "chat": chat, "replys" : no_of_replys})


@login_required
def delete_chat(request, chat_id):
    chat = Chat.objects.get(pk=chat_id)
    return HttpResponse("<h1>Attempting to delete chat</h1>")


@login_required
def load_send_custom_message(request):   
    return render(request, 'messaging/load_custom_send_message.html')

@login_required
def load_custom_reply_message(request, chat_id, message_id):
    chat = Chat.objects.get(pk=chat_id)
    message = Message.objects.get(pk=message_id)
    return render(request, 'messaging/load_custom_reply_message.html', {'message': message, 'chat' : chat})
    

@login_required
def send_custom_message_get(request, chat_id):
    print(chat_id)
    chat_id=chat_id
    receivers = CustomUser.objects.exclude(pk=request.user.pk)
    return render(request, 'messaging/load_custom_send_message.html', {'receivers': receivers, 'chat_id': chat_id})

@login_required
def send_custom_message_post(request, chat_id):
    if request.method == 'POST':
        chat = None
        x=Chat.objects.get(pk=chat_id)
        try:
            #check if the other user has created a chat
            y=Chat.objects.get(sender=x.receiver, receiver=x.sender)
            #delete the newer chat
            if(y.id< x.id):
                delete_chat(request, x.id)
                print("chat deleted")
                chat=y
                
            else:
                print(x.id)
                chat=x
                delete_chat(request, y.id)
                print("chat deleted")
        except:
            chat=x
            
        message_content = request.POST.get('message_content')

        #track who send the message
        sender=request.user
        color = 10
        #logged in user created the chat
        if sender.id == chat.sender.id:
            sender.color = 1
            color=sender.color
            print(sender.color)
        else:
            sender.color = 0
            color=sender.color
            
        #send the message
        Message.objects.create(content=message_content, chat=chat, color=color)
        messages = Message.objects.filter(chat=chat.id)
        
        return render(request, 'messaging/open_chat.html', {"messages": messages, "chat": chat})  # Redirect to dashboard after sending message
    else:
        # Handle other cases (optional)
        pass

        

@login_required
def send_custom_reply_message(request, chat_id, message_id):
    if request.method == 'POST':
        chat = None
        x=Chat.objects.get(pk=chat_id)
        try:
            #check if the other user has created a chat
            y=Chat.objects.get(sender=x.receiver, receiver=x.sender)
            #delete the newer chat
            if(y.id< x.id):
                delete_chat(request, x.id)
                print("chat deleted")
                chat=y
                
            else:
                print(x.id)
                chat=x
                delete_chat(request, y.id)
                print("chat deleted")
        except:
            chat=x
            
        message_content = request.POST.get('message_content')

        #track who send the message
        sender=request.user
        color = 10
        #logged in user created the chat
        if sender.id == chat.sender.id:
            sender.color = 1
            color=sender.color
            print(sender.color)
        else:
            sender.color = 0
            color=sender.color
            
        #send the message
        Message.objects.create(content=message_content, chat=chat, color=color, parent=message_id)
        messages = Message.objects.filter(chat=chat.id)
        
        return render(request, 'messaging/open_chat.html', {"messages": messages, "chat": chat})  # Redirect to dashboard after sending message
    else:
        # Handle other cases (optional)
        pass


def delete_chat(request, chat_id):
    try:
        chat = get_object_or_404(Chat, pk=chat_id)
        chat.delete()
        print("Chat deleted successfully!")  # You can customize the response as needed
    except Exception as e:
        print("Status 500")
 
def delete_view_chat(request, chat_id):
    try:
        chat = get_object_or_404(Chat, pk=chat_id)
        chat.delete()
        user_chats = Chat.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
        return render(request, 'messaging/view_chats.html', {'user_chats': user_chats})
    except Exception as e:
        print("Status 500")
        
        
def delete_message(request, message_id):

    try:
        message = get_object_or_404(Message, pk=message_id)
        print(message)
        message.delete()
        #load the chats related to the user
        user_chats = Chat.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
        return render(request, 'messaging/view_chats.html', {'user_chats': user_chats})
    except Exception as e:
        print("Status 500")
        