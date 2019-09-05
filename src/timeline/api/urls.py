from django.urls import path
from .views import MessageAPIView, MessageCreateView, MessageAPIRUDView


app_name = 'api-messages'
urlpatterns = [
    path('messages/all/', MessageAPIView.as_view(), name='messages-list'),
    path('message/new/', MessageCreateView.as_view(), name='message-create'),
    path('message/<slug:slug>/', MessageAPIRUDView.as_view(), name='message-rud'),
]
