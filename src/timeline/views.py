from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Message


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message
