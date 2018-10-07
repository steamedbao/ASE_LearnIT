from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, reverse

from accounts.views import ProfileDetailView, RegisterUserView
from questions.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('search', IndexView.as_view(), name='search'),

    path('accounts/register', RegisterUserView.as_view(), name='register'),
    path('accounts/login',
         LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/login',
         LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('profiles/<slug:slug>', ProfileDetailView.as_view(), name='profile'),

    path('questions/', include('questions.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__', include(debug_toolbar.urls)),)
