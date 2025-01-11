from django.forms import ValidationError
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
    attendees_count = models.IntegerField(default=0)

    def clean(self):
        if self.status != 'active' and self.attendees_count > 0:
            raise ValidationError("Event cannot have attendees if it's not active.")

    def available_slots(self):
        """
        Calculate available slots for the event.
        """
        return self.capacity - self.attendees_count

    def is_full(self):
        """
        Check if the event is full.
        """
        return self.available_slots() <= 0
    def is_registered(self, email):
        """
        Check if an email is already registered for the event.
        """
        return self.attendees.filter(email=email).exists()

    def is_waitlisted(self, email):
        """
        Check if an email is already on the waitlist for the event.
        """
        return self.waitlist.filter(email=email).exists()
    def move_from_waitlist(self):
        """
        Move the first person from the waitlist to attendees if a slot is available.
        """
        if not self.is_full() and self.waitlist.exists():
            first_in_waitlist = self.waitlist.first()
            Attendee.objects.create(
                name=first_in_waitlist.name,
                email=first_in_waitlist.email,
                event=self
            )
            self.attendees_count += 1
            self.save()
            first_in_waitlist.delete()
    
    def __str__(self):
        return self.title


class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendees")

    class Meta:
        unique_together = ('email', 'event')  # Prevent duplicate attendees

    def __str__(self):
        return f"{self.name} attending {self.event.title}"


class Waitlist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="waitlist")

    class Meta:
        unique_together = ('email', 'event')  # Prevent duplicate waitlist entries

    def __str__(self):
        return f"{self.name} on waitlist for {self.event.title}"
