from rest_framework import serializers
from timeline.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_username_from_author')
    comments = serializers.SerializerMethodField('get_text_from_comments')

    class Meta:
        model  = Message
        fields = ['slug', 'body', 'date_created', 'date_published', 'author', 'comments']

    def get_username_from_author(self, message):
        username = message.author.username
        return username

    def get_text_from_comments(self, message):
        comment_text = [{'comment text': msg.text, 'comment author': msg.author.username}
                            for msg in message.comments.all()]
        return comment_text
