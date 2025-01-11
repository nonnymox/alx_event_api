from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Event
from .serializers import EventSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Event, Attendee, Waitlist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AttendeeSerializer, WaitlistSerializer
# View for listing events
class EventListView(generics.ListAPIView):
    """
    Retrieve a list of all events. All users can see all events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]


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

class EventRegisterView(APIView):
    """
    Handle attendee registration for an event.
    - Registers attendees if the event is not full.
    - Adds attendees to the waitlist if the event is full and waitlist is enabled.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # Retrieve the event by its title
        event_title = request.data.get("event")
        event = get_object_or_404(Event, title=event_title)

        # Check if the event is full
        if event.is_full():
            # Handle waitlist registration  automatically
                return self.add_to_waitlist(request, event)

        # Handle regular attendee registration
        return self.register_attendee(request, event)

    def register_attendee(self, request, event):
        """
        Registers an attendee for an event if it's not full.
        """
        serializer = AttendeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event)  # Save attendee to the event
            event.attendees_count += 1  # Increment attendee count
            event.save()
            return Response(
                {"message": "Successfully registered for the event."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_to_waitlist(self, request, event):
        """
        Adds an attendee to the waitlist for an event if it's full.
        """
        serializer = WaitlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event)  # Save attendee to the waitlist
            return Response(
                {"message": "Event is full. Added to the waitlist."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventCapacityView(APIView):
    """
    Get the capacity and attendee details for an event.
    """

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return Response({
            "capacity": event.capacity,
            "attendees_count": event.attendees_count,
            "available_slots": event.available_slots()
        }, status=status.HTTP_200_OK)


class WaitlistView(APIView):
    """
    View the waitlist for an event.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        waitlist = Waitlist.objects.filter(event=event)
        serializer = WaitlistSerializer(waitlist, many=True)
        return Response({"waitlist": serializer.data}, status=status.HTTP_200_OK)
