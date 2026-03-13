from django.shortcuts import render,redirect
from doctors.models import Availability
from .models import Booking
from django.db import transaction
from accounts.models import User
import requests

def patient_dashboard(request):

    return render(request,'patient_dashboard.html')

def doctor_list(request):

    doctors = User.objects.filter(role="doctor")

    return render(request, "doctor_list.html", {"doctors": doctors})

def view_slots(request,doctor_id):

    slots=Availability.objects.filter(
    doctor=doctor_id,
    is_booked=False
    )

    return render(request,'slots.html',{'slots':slots})

def book_slot(request, slot_id):

    with transaction.atomic():
        slot = Availability.objects.select_for_update().get(id=slot_id)

        if not slot.is_booked:
            Booking.objects.create(
                patient=request.user,
                slot=slot
            )
            slot.is_booked = True
            slot.save()

            # Try calling email service but don't break the page if it's down
            try:
                requests.post(
                    "http://localhost:3000/dev/send",
                    json={"action": "BOOKING_CONFIRMATION"},
                    timeout=2
                )
            except Exception:
                print("Email service not running")

    return redirect('my_bookings')
def my_bookings(request):

    bookings=Booking.objects.filter(patient=request.user)

    return render(request,'my_bookings.html',{'bookings':bookings})