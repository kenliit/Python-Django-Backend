from django.http import Http404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event
from rating.serializers import ImageOrVideoSerializer


# class ImageOrVideoEventView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [IsAuthenticated]
#
#     def get_list(self, event_id):
#         try:
#             event = Event.objects.get(id=event_id)
#             return event.image_or_videos.all()
#         except Event.DoesNotExist:
#             raise Http404
#
#     def get(self, request, event_id, format=None):
#         items = self.get_list(event_id)
#         serializer = ImageOrVideoSerializer(items, many=True)
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#     def delete(self, request, event_id, format=None):
#         items = self.get_list(event_id)
#         items.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)










