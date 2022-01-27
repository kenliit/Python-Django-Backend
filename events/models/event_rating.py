from rating.models import Thumb, Comment
from .event_models import Event
from django.db import models


class EventThumb(Thumb):
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.theme[:50] + " - " + str(self.like)


class EventComment(Comment):
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.theme[:30] + " - " + str(self.content)



















