from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from events.models import Event
from locations.serializers import LocationSerializer

User = get_user_model()


class EventSerializer(ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Event
        fields = ['user', 'host', 'theme', 'description', 'event_type',
                  'for_age', 'start-date', 'end-date', 'open', 'close', 'location']





