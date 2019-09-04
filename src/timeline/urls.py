from django.urls import path
from .views import MessageListView, MessageDetailView


app_name    = 'timeline'
urlpatterns = [
    path('messages/', MessageListView.as_view(), name='list'),
    path('message/<slug:slug>/', MessageDetailView.as_view(), name='single'),
]
