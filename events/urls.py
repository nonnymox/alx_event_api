from django.urls import path
from .views import (
    EventListView,
    EventCreateView,
    EventRetrieveUpdateDestroyView,
    EventRegisterView,
    EventCapacityView,
    WaitlistView
)

urlpatterns = [
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event_detail'),
    path('events/<int:event_id>/register/', EventRegisterView.as_view(), name='event_register'),
    path('events/<int:event_id>/capacity/', EventCapacityView.as_view(), name='event_capacity'),
    path('events/<int:event_id>/waitlist/', WaitlistView.as_view(), name='event_waitlist'),
]
