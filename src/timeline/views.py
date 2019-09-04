from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from .forms import MessageForm


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model      = Message
    form_class = MessageForm

    def form_valid(self, form):
        self.object        = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
