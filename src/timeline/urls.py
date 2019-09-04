from django.urls import path
from .views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    MessagePublishView,
    DraftListView,
    CommentAtMessageView,
    CommentApproveView,
    CommentRemoveView,
)


app_name    = 'timeline'
urlpatterns = [
    path('messages/', MessageListView.as_view(), name='list'),
    path('message/new/', MessageCreateView.as_view(), name='create'),
    path('message/<slug:slug>/remove/', MessageDeleteView.as_view(), name='remove'),
    path('message/<slug:slug>/edit/', MessageUpdateView.as_view(), name='edit'),
    path('message/<slug:slug>/', MessageDetailView.as_view(), name='single'),

    path('messages/drafts/', DraftListView.as_view(), name='drafts_list'),
    path('message/<slug:slug>/publish/', MessagePublishView.as_view(), name='publish'),
    path('message/<slug:slug>/comment/', CommentAtMessageView.as_view(), name='new_comment'),
    path('message/<slug:slug>/comment/<int:pk>/approve/', CommentApproveView.as_view(), name='comment_approve'),
    path('message/<slug:slug>/comment/<int:pk>/remove/', CommentRemoveView.as_view(), name='comment_remove'),
]
