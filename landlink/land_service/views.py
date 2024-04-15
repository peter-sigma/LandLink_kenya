# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LandService, LawyerService
from .forms import AddServiceForm
from .forms import UpdateServiceForm

@login_required
def select_service(request):
    if request.method == 'POST':
        # Handle form submission to update costs for lawyer services
        selected_service_id = request.POST.get('service')
        cost = request.POST.get('cost')
        
        # Get the selected service object
        service = LandService.objects.get(pk=selected_service_id)
        
        # Check if the lawyer already has this service
        lawyer_service = LawyerService.objects.filter(lawyer=request.user, service=service).first()
        if lawyer_service:
            # Update the cost if the service already exists for the lawyer
            lawyer_service.cost = cost if cost else service.cost
            lawyer_service.save()
        else:
            # Create a new LawyerService instance if the service doesn't exist for the lawyer
            LawyerService.objects.create(lawyer=request.user, service=service, cost=cost if cost else service.cost)
        
        # Redirect back to the select_service page
        return redirect('select_service')
    else:
        # Retrieve available services and lawyer's services
        services = LandService.objects.all()
        lawyer_services = LawyerService.objects.filter(lawyer=request.user)
        return render(request, 'land_service/select_service.html', {'services': services, 'lawyer_services': lawyer_services})



    
@login_required
def add_service(request):
    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            # Get the current user
            user = request.user
            
            # Check if the user is a lawyer
            if user.user_type == 'lawyer':
                # If user is a lawyer, add the service
                name = form.cleaned_data['name']
                cost = form.cleaned_data['cost']
                
                # Check if the service already exists
                existing_service = LandService.objects.filter(name=name).exists()
                if existing_service:
                    # If the service already exists, display an error message
                    form.add_error('name', 'Service with this name already exists.')
                else:
                    # Create LandService instance
                    LandService.objects.create(name=name, cost=cost)

                    # Redirect to select_service
                    return redirect('select_service')
                
            else:
                # If user is not a lawyer, redirect them to the appropriate dashboard
                if user.user_type == 'seller':
                    return redirect('seller_dashboard')
                elif user.user_type == 'buyer':
                    return redirect('buyer_dashboard')
    else:
        form = AddServiceForm()
    
    return render(request, 'land_service/add_service.html', {'form': form})


@login_required
def lawyer_services(request):
    # Retrieve all services belonging to the lawyer
    lawyer_services = LawyerService.objects.filter(lawyer=request.user)
    return render(request, 'land_service/lawyer_services.html', {'lawyer_services': lawyer_services})



@login_required
def update_service(request, service_id):
    service = get_object_or_404(LawyerService, pk=service_id)
    if request.method == 'POST':
        form = UpdateServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('lawyer_services')
        else:
            print("Bad Thing happened")
    else:
        form = UpdateServiceForm(instance=service)
    return render(request, 'land_service/update_service.html', {'form': form})