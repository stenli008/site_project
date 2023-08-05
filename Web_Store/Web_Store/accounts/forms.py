from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from Web_Store.accounts.models import CustomerUser


class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomerUser
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'})
    )
