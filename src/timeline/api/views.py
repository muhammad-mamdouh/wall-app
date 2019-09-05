from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import CreateModelMixin
from django.db.models import Q
from django.views.generic import TemplateView
from timeline.models import Message
from .serializers import MessageSerializer
from .permissions import IsOwnerOrReadOnly


class MessageAPIView(CreateModelMixin, ListAPIView):
    """
    API endpoint that have the ability to:
        1. Lists all of the created messages with its inner comments.
        2. Enables users to share new messages with others.
    """
    queryset         = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer
    lookup_field     = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        query_set = Message.objects.all()
        query     = self.request.GET.get('q')
        if query is not None:
            query_set = query_set.filter(Q(title__icontains=query)|Q(body__icontains=query)).distinct()
        return query_set

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


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
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class MessageAPITutorial(TemplateView):
    template_name = 'api/doc.html'
