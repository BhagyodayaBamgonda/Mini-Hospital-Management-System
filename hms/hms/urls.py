from django.contrib import admin
from django.urls import path,include
from accounts.views import home

urlpatterns=[
path('admin/',admin.site.urls),
path('',home),

path('',include('accounts.urls')),
path('',include('doctors.urls')),
path('',include('bookings.urls')),
]