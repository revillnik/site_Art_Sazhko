from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
)

from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from users.forms import RegisterUserForm, LoginUserForm, ProfileUserForm
from django.contrib.auth.views import LoginView


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = "login"


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class ProfileUser(UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "users/profile.html"

    def get_success_url(self):
        return reverse_lazy("profile", args=(self.request.user.id,))
