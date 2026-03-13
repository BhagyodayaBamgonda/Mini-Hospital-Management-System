from django.urls import path
from . import views

urlpatterns = [
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('add-slot/', views.add_slot, name='add_slot'),
    path('doctor_bookingd/', views.doctor_bookings, name='doctor_bookings')
]