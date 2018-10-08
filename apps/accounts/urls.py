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
    path('register', RegisterUserView.as_view(), name='register'),
    path('login',
         LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('login',
         LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('profiles/<slug:slug>', ProfileDetailView.as_view(), name='profile'),
    path('profiles/<slug:slug>/edit',
         ProfileUpdateView.as_view(), name='edit_profile'),
    path('<int:pk>/edit',
         AccountUpdateView.as_view(), name='edit_account'),
]
