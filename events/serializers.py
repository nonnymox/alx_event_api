from rest_framework import serializers
from .models import Event, Attendee, Waitlist


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')  # Display the username
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['organizer', 'created_at']  # Ensure `created_by` and `created_at` are read-only

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'event']

class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ['name', 'email', 'event']
