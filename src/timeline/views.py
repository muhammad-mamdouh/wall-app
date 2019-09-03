from django.views.generic import (
    ListView,
)
from .models import Message


class MessageListView(ListView):
    model = Message
