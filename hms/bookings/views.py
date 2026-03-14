from django.shortcuts import render, redirect
from doctors.models import Availability
from .models import Booking
from django.db import transaction
from accounts.models import User
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_service():

    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )

        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)

    return service


def create_calendar_event(summary, start, end):

    service = get_calendar_service()

    event = {
        "summary": summary,
        "start": {
            "dateTime": start
        },
        "end": {
            "dateTime": end
        }
    }

    event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    print("Event created:", event.get("htmlLink"))


def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')


def doctor_list(request):

    doctors = User.objects.filter(role="doctor")

    return render(request, "doctor_list.html", {"doctors": doctors})


def view_slots(request, doctor_id):

    slots = Availability.objects.filter(
        doctor=doctor_id,
        is_booked=False
    )

    return render(request, 'slots.html', {'slots': slots})


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

            # -------- GOOGLE CALENDAR EVENT --------

            try:

                start_dt = datetime.combine(slot.date, slot.start_time)
                end_dt = datetime.combine(slot.date, slot.end_time)

                start = start_dt.strftime("%Y-%m-%dT%H:%M:%S") + "+05:30"
                end = end_dt.strftime("%Y-%m-%dT%H:%M:%S") + "+05:30"

                print("START:", start)
                print("END:", end)

                create_calendar_event(
                    f"Doctor Appointment with Dr. {slot.doctor.username}",
                    start,
                    end

                )

            except Exception as e:
                print("Calendar event failed:", e)

            # -------- SERVERLESS EMAIL --------

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

    bookings = Booking.objects.filter(patient=request.user)

    return render(request, 'my_bookings.html', {'bookings': bookings})