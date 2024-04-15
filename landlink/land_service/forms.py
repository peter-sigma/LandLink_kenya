# forms.py
from django import forms
from .models import LawyerService
from land_service.models import LandService  # Assuming the LandService model exists in the land_service app

class SelectServiceForm(forms.ModelForm):
    class Meta:
        model = LawyerService
        fields = ['service', 'cost']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Query the LandService model to get existing services
        existing_services = LandService.objects.all()
        self.fields['service'].queryset = existing_services

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = LandService
        fields = ['name', 'cost']
        widgets = {
            'cost': forms.NumberInput(attrs={'min': 0}),
        }
        

class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model = LawyerService
        fields = ['service', 'cost']
        widgets = {
            'cost': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the service field as read-only
        self.fields['service'].widget.attrs['readonly'] = True
