from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required



def custom_signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Form errors:", form.errors)  # Debug output
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/registration.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.user_type == 'buyer':
                return redirect('buyer_dashboard')
            elif user.user_type == 'seller':
                return redirect('seller_dashboard')
            elif user.user_type == 'lawyer':
                return redirect('lawyer_dashboard')
            else:
                return redirect('home')  # Redirect unknown user_type to homepage
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})



def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def buyer_dashboard(request):
    return render(request, 'account/buyer_dashboard.html')

@login_required
def seller_dashboard(request):
    return render(request, 'account/seller_dashboard.html')

@login_required
def lawyer_dashboard(request):
    return render(request, 'account/lawyer_dashboard.html')