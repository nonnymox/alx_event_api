from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Event
from .serializers import EventSerializer

# View for listing events
class EventListView(generics.ListAPIView):
    """
    Retrieve a list of all events. Authenticated users can see all events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# View for creating events
class EventCreateView(generics.CreateAPIView):
    """
    Allow authenticated users to create new events.
    Automatically sets the 'created_by' field to the logged-in user.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)  # Set `created_by` to the authenticated user


# View for retrieving, updating, and deleting events
class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific event.
    Users can only update or delete events they created.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Ensure that only the creator of the event can update it
        event = self.get_object()
        if event.organizer != request.user:
            raise PermissionDenied("You do not have permission to edit this event.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Ensure that only the creator of the event can delete it
        event = self.get_object()
        if event.organizer != request.user:
            raise PermissionDenied("You do not have permission to delete this event.")
        return super().destroy(request, *args, **kwargs)
