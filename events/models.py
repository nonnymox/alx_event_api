from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)  # Optional time field
    location = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('canceled', 'Canceled'), ('completed', 'Completed')], default='active')  # Event status
    category = models.CharField(max_length=100, null=True, blank=True)  # Optional category field
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)  # Optional image field for events

    def __str__(self):
        return self.title
