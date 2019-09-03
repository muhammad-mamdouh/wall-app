from django.urls import path
from .views import MessageListView


app_name    = 'timeline'
urlpatterns = [
    path('messages/', MessageListView.as_view(), name='list'),
]
