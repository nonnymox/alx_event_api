# Generated by Django 5.1.4 on 2025-01-10 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_rename_organizer_event_organizer1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='organizer1',
            new_name='organizer',
        ),
    ]
