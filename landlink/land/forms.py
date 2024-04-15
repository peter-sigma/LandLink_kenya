# forms.py
from django import forms
from .models import Land

class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['title', 'description', 'image', 'price']  # Add all the fields you want to include in the form
