from rest_framework import serializers
from timeline.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_username_from_author')
    comments = serializers.SerializerMethodField('get_text_from_comments')

    class Meta:
        model  = Message
        fields = ['slug', 'title', 'body', 'date_created', 'date_published', 'author', 'comments']
        read_only_fields = ['slug', 'date_created', 'author', 'comments']

    def validate_title(self, value):
        query_set = Message.objects.filter(title__iexact=value)
        if self.instance:
            query_set = query_set.exclude(slug=self.instance.slug)
        if query_set.exists():
            raise serializers.ValidationError('A message with this title has already been shared!')
        return value

    def get_username_from_author(self, message):
        username = message.author.username
        return username

    def get_text_from_comments(self, message):
        comment_text = [{'comment text': msg.text, 'comment author': msg.author.username}
                            for msg in message.comments.all()]
        return comment_text
