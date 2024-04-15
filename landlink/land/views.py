from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Land
from .forms import LandForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def home(request):
    return render(request, "land/index.html")


def land_detail(request, land_id):
    # Retrieve land object and other necessary data
    land = Land.objects.get(id=land_id)
    receiver_id = land.owner.id  # Assuming the seller is the receiver of the message
    return render(request, 'land/land_detail.html', {'land': land, 'receiver_id': receiver_id})

def add_land(request):
    if request.method == 'POST':
        form = LandForm(request.POST, request.FILES)
        if form.is_valid():
            land = form.save(commit=False)
            land.owner = request.user  # Set the owner to the currently logged-in user
            land.save()
            return redirect('seller_dashboard')  # Redirect to home page or any other page
    else:
        form = LandForm()
    return render(request, 'land/add_land.html', {'form': form})

@csrf_exempt
def update_location(request, land_id):
    print('Request received:', request.method)
    if request.method == 'POST':
        print(request.POST)
        try:
            land = Land.objects.get(pk=land_id)
        except Land.DoesNotExist:
            return JsonResponse({'status': 'Error: Land object does not exist'}, status=404)

        print(latitude, longitude)
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if latitude is not None and longitude is not None:
            land.latitude = latitude
            land.longitude = longitude
            land.save()
            return JsonResponse({'status': 'Location updated successfully'})
        else:
            return JsonResponse({'status': 'Error: Latitude or longitude is missing'}, status=400)
    else:
        return JsonResponse({'status': 'Error: Only POST requests are allowed'}, status=405)

def update_location_view(request, land_id=4):
    land = Land.objects.get(id=land_id)
    return render(request, 'land/update_location.html', {'land': land})