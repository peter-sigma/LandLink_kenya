from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'user_type', 'email', 'password1', 'password2')
