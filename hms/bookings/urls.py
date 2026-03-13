from django.urls import path
from . import views

urlpatterns = [
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctors/', views.doctor_list, name='doctors'),
    path('slots/<int:doctor_id>/', views.view_slots, name='slots'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
]