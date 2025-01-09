from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='created_by.username')  # Display the username
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['organizer', 'created_at']  # Ensure `created_by` and `created_at` are read-only
