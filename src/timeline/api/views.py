from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from timeline.models import Message
from .serializers import MessageSerializer


class MessageAPIView(ListAPIView):
    """
    API endpoint that lists all of the created messages with its inner comments.
    """
    queryset         = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer


class MessageCreateView(CreateAPIView):
    """
    API endpoint that enables users to share new messages with others.
    """
    queryset         = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessageAPIRUDView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint that gives you the ability to
        1. Read/Retrieve a specific message with its inner comments.
        2. Update it.
        3. Delete it.
    """
    queryset         = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer
    lookup_field     = 'slug'
