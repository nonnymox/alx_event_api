# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from .models import Event
# from .serializers import EventSerializer
# # events/views.py


# class CreateEventView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(created_by=request.user)
#             return Response({
#                 'id': serializer.data['id'],
#                 'message': 'Event created successfully.'
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class EventListView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# 
from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer

# View for listing events
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# View for creating events
class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        # Automatically set the `created_by` field to the currently authenticated user
        serializer.save(created_by=self.request.user)

# View for retrieving, updating, and deleting events
class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
