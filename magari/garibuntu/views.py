from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import CarGroup, Event, EventRegistration
from events.forms import EventRegistrationForm
from sponsors.models import Sponsor
from django.contrib.auth import logout


# Create your views here.

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user':user})

def car_group_list(request):
    groups = CarGroup.objects.all()
    return render(request, 'car-groups-list.html', {'groups':groups})


def car_group_detail(request, group_id):
    car_group = get_object_or_404(CarGroup, pk=group_id)
    return render(request, 'car_group_detail.html', {'car_group': car_group})

def car_group_dash(request, group_id):
    car_group = get_object_or_404(CarGroup, pk=group_id)

    members = car_group.members.all()

    return render(request, 'dash-car-group.html', {'car_group': car_group, 'members':members})



def event_list(request):
    events = Event.objects.all()
    user = request.user
    payment_status = EventRegistration.payment_status
    return render(request, 'dash-events.html', {'events':events, 'payment_status':payment_status})

def group_list_dash(request):
    car_groups = CarGroup.objects.all()
    return render(request, 'dash-groups.html', {'car_groups':car_groups})

def master_register(request):
    return render(request, 'master_registration.html')

@login_required
def event_register(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = EventRegistrationForm()

    if EventRegistration.objects.filter(user=request.user, event=event).exists():
        messages.info(request, 'You have already registered for this event')
        return redirect('garibuntu:event_list')
    
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.event = event
            registration.save()
            messages.success(request, 'You have successfully been registered.')
            return redirect('events:event_list')
        else:
            form = EventRegistrationForm()

    return render(request, 'dash-events-reg.html', {'form':form, 'event':event})



def sponsor_list(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'dash-sponsor-list.html', {'sponsors':sponsors})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('garibuntu:home')  # Redirect to the login page or any other page