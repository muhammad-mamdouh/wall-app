from django import forms
from .models import Message, Comment


class MessageForm(forms.ModelForm):
    class Meta:
        model   = Message
        fields  = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'body': forms.Textarea(attrs={'class': 'editable medium-editor-textarea messagecontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
