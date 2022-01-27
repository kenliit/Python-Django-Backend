from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from locations.models import Location
from users.models import AgeType
from rating.models import ImageOrVideo

User = get_user_model()


class Event(models.Model):
    class EventType(models.TextChoices):
        Live = 'Live'
        Online = 'Online'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    host = models.CharField(max_length=100, null=False)
    theme = models.CharField(max_length=300, null=False)
    description = models.TextField(max_length=1000, null=False)
    event_type = models.CharField(max_length=10, blank=False, choices=EventType.choices, default=EventType.Live)
    for_age = models.CharField(max_length=1, blank=False, choices=AgeType.choices, default=AgeType.Adult)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    open = models.TimeField(null=False)
    close = models.TimeField(null=False)
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=False, default=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.user.name + " - " + self.theme[:30]


class EventIOV(ImageOrVideo):
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    is_primary = models.BooleanField(null=False, default=True)

    class Meta:
        ordering = ("event", "is_primary")

    def __str__(self):
        return f"{self.event.theme[:50]}"

    def save(self, *args, **kwargs):
        if self.is_primary:
            EventIOV.objects.filter(event=self.event).update(is_primary=False)
        super(EventIOV, self).save(*args, **kwargs)

















