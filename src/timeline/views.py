from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
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


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model       = Message
    success_url =  reverse_lazy('timeline:list')

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Message has been deleted successfully!')
        return super().delete(*args, **kwargs)
