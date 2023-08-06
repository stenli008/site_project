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


class CustomerUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')
        exclude = ('password', )
        labels = {
            'username': 'Username: ',
            'first_name': 'First Name: ',
            'last_name': 'Last Name: ',
            'email': 'Email: ',
            'profile_picture': 'Profile Picture: '
        }