from django.urls import path
from .views import MessageAPIView


app_name = 'api-messages'
urlpatterns = [
    path('messages/all/', MessageAPIView.as_view(), name='messages-list'),
]
