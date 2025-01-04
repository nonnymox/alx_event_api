from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Removed './'
    path('events/', include('events.urls')),  # Removed './'
    path('', home),  # Add this line for the root URL
]
