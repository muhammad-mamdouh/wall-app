from django.urls import path
from .views import MessageAPIView, MessageAPIRUDView


app_name = 'api-messages'
urlpatterns = [
    path('messages/', MessageAPIView.as_view(), name='messages-list-create'),
    path('message/<slug:slug>/', MessageAPIRUDView.as_view(), name='message-rud'),
]
