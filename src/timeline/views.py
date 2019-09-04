from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Message
from .forms import MessageForm


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        return Message.objects.filter(date_published__isnull=False).order_by('-date_published')



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


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model         = Message
    form_class    = MessageForm
    extra_context = {'message_edit': 'valid'}

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('timeline:single', kwargs={'slug': self.kwargs.get('slug')})


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model       = Message
    success_url =  reverse_lazy('timeline:list')

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Message has been deleted successfully!')
        return super().delete(*args, **kwargs)


class DraftListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {'draft_messages': 'draft'}

    def get_queryset(self):
        return Message.objects.filter(date_published__isnull=True).order_by('-date_created')

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('timeline:single', kwargs={'slug': self.kwargs.get('slug')})
