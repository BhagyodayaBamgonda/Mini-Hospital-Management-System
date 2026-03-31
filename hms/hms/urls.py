from django.contrib import admin
from django.urls import path,include
from accounts.views import home
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
path('admin/',admin.site.urls),
path('',home),

path('',include('accounts.urls')),
path('',include('doctors.urls')),
path('',include('bookings.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)