from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from .views import (AccountUpdateView, ProfileDetailView, ProfileUpdateView,
                    RegisterUserView)

urlpatterns = [
    path('accounts/register', RegisterUserView.as_view(), name='register'),
    path('accounts/login/',
         LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout', LogoutView.as_view(next_page='/'), name='logout'),

    path('profiles/<slug:slug>', ProfileDetailView.as_view(), name='profile'),
    path('profiles/<slug:slug>/edit',
         ProfileUpdateView.as_view(), name='edit_profile'),
    path('accounts/edit',
         AccountUpdateView.as_view(), name='edit_account'),
]
