from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views


app_name    = 'account'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Password Change Links
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done'),
                                              template_name='account/password_change.html'),
        name='password_change',
    ),
    path(
        'password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
         name='password_change_done'
    ),
]
