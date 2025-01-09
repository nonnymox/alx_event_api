from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name="events")
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('canceled', 'Canceled'), ('completed', 'Completed')], default='active')  # Event status
    category = models.CharField(max_length=100, null=True, blank=True)  # Optional category field
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)  # Optional image field for events
    capacity = models.PositiveIntegerField(default=200)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
