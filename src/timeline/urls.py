from django.urls import path
from .views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    DraftListView,
)


app_name    = 'timeline'
urlpatterns = [
    path('messages/', MessageListView.as_view(), name='list'),
    path('message/new/', MessageCreateView.as_view(), name='create'),
    path('message/<slug:slug>/remove/', MessageDeleteView.as_view(), name='remove'),
    path('message/<slug:slug>/edit/', MessageUpdateView.as_view(), name='edit'),
    path('message/<slug:slug>/', MessageDetailView.as_view(), name='single'),

    path('messages/drafts/', DraftListView.as_view(), name='drafts_list'),
]
