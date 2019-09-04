from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserSignUpForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label    = 'Email Address'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(f'Email: {user.email} is already in use.')

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(f'Username: {account.username} is already in use.')
