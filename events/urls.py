# events/urls.py
from django.urls import path
from .views import EventListView, EventCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),  # URL for listing events
    path('events/create', EventCreateView.as_view(), name='event-create'),  # URL for creating events
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),  # URL for retrieving, updating, and deleting events
]
