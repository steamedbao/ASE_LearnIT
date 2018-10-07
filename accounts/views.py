from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from .forms import RegisterForm
from .models import Profile


# Create your views here.
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'


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
