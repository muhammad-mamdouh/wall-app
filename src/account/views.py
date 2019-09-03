from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserSignUpForm


class SignUpView(CreateView):
    form_class    = UserSignUpForm
    success_url   = reverse_lazy('account:login')
    template_name = 'account/signup.html'
