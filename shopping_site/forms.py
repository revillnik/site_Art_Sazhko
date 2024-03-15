from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from django.contrib.auth import get_user_model


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-group mb-6"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-group mb-6"})
    )
    password2 = forms.CharField(
        label=" Проверка пароля",
        widget=forms.PasswordInput(attrs={"class": "form-group mb-6"}),
    )

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "email": "E-mail",
        }
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-group mb-6"}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class ProfileUserForm(UserChangeForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-group mb-6",
            }
        ),
    )
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-group mb-6",
            }
        ),
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={
                "class": "form-group mb-6",
            }
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(
            attrs={
                "class": "form-group mb-6",
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email"]


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]
