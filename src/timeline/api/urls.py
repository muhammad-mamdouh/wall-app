from django.urls import path
from .views import MessageAPIView, MessageAPIRUDView


app_name = 'api-messages'
urlpatterns = [
    path('messages/all/', MessageAPIView.as_view(), name='messages-list'),
    path('message/<slug:slug>/', MessageAPIRUDView.as_view(), name='message-rud'),
]
