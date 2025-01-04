# events/urls.py

from django.urls import path
from .views import EventListView, CreateEventView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),  # Event list URL
    path('create/', CreateEventView.as_view(), name='create_event'),
]
