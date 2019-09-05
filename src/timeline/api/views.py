from rest_framework.generics import ListAPIView
from timeline.models import Message
from .serializers import MessageSerializer


class MessageAPIView(ListAPIView):
    """
    API endpoint that lists all of the created messages with its inner comments.
    """
    queryset         = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer
