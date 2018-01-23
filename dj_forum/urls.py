from django.urls import path
from django.urls import reverse
from django.contrib import admin
from forum import views as forum_views
from accounts.views import ProfileDetailView, RegisterUserView
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('accounts/register', RegisterUserView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout', LogoutView.as_view(next_page='/'), name='logout'),

    path('profiles/<slug:slug>', ProfileDetailView.as_view(), name='profile'),

    path('', forum_views.IndexView.as_view(), name='index'),

    path('categories/<slug:slug>', forum_views.CategoryDetailView.as_view(), name='category'),

    path('questions/new', forum_views.QuestionCreateView.as_view(), name='new_question'),
    path('questions/<slug:slug>', forum_views.QuestionDetailView.as_view(), name='question'),

    path('admin/', admin.site.urls),
]
