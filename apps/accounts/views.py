from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView

from .forms import ProfileForm, RegisterForm
from .models import Profile


# Create your views here.
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/account_edit.html'

    def get_object(self):
        return self.request.user


class RegisterUserView(FormView):
    template_name = 'accounts/register.html'
    success_url = '/'
    form_class = RegisterForm

    def form_valid(self, form):
        user = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1']
        )

        return super(RegisterUser, self).form_valid(form)
