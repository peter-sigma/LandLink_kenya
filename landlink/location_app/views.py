from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Location

def add_location(request, land_id):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_location')
    else:
        form = LocationForm()
    return render(request, 'location_app/add_location.html', {'form': form})


def view_location(request, location_id):
    # Retrieve the location object by its ID
    location = Location.objects.get(id=location_id)
    # Construct the Google Maps URL
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={location.latitude},{location.longitude}"
    # Redirect the user to Google Maps
    return redirect(google_maps_url)