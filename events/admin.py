# event/admin.py
from django.contrib import admin
from .models import Event, Attendee, Waitlist

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "organizer", "date_time", "capacity", "attendees_count", "status")
    list_filter = ("status", "date_time", "organizer")
    search_fields = ("title", "organizer__username")
    readonly_fields = ("created_at",)

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event")
    list_filter = ("event",)
    search_fields = ("name", "email", "event__title")

@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event")
    list_filter = ("event",)
    search_fields = ("name", "email", "event__title")

