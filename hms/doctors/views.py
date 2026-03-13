from django.shortcuts import render,redirect
from .models import Availability
from bookings.models import Booking

def doctor_dashboard(request):

    slots=Availability.objects.filter(doctor=request.user)

    return render(request,'doctor_dashboard.html',{'slots':slots})

def add_slot(request):

    if request.method=='POST':

        date=request.POST['date']
        start=request.POST['start']
        end=request.POST['end']

        Availability.objects.create(
        doctor=request.user,
        date=date,
        start_time=start,
        end_time=end
        )

        return redirect('doctor_dashboard')

    return render(request,'add_slot.html')

def doctor_bookings(request):

    bookings=Booking.objects.filter(slot__doctor=request.user)

    return render(request,'doctor_bookings.html',{'bookings':bookings})