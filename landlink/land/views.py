from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Land

def home(request):
    return render(request, "land/index.html")


def land_detail(request, land_id):
    # Retrieve land object and other necessary data
    land = Land.objects.get(id=land_id)
    receiver_id = land.owner.id  # Assuming the seller is the receiver of the message
    return render(request, 'land/land_detail.html', {'land': land, 'receiver_id': receiver_id})

