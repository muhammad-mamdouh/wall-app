from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm, UserUpdateForm

class SignUpView(CreateView):
    form_class    = UserSignUpForm
    success_url   = reverse_lazy('account:login')
    template_name = 'account/signup.html'


@login_required()
def profile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)

        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('account:profile')
    else:
        update_form = UserUpdateForm(instance=request.user)

    return render(request, 'account/profile.html', {'update_form': update_form})
