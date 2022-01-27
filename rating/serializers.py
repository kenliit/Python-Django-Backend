from rest_framework.serializers import ModelSerializer
from rating.models import ImageOrVideo


class ImageOrVideoSerializer(ModelSerializer):

    class Meta:
        model = ImageOrVideo
        fields = '__all__'















