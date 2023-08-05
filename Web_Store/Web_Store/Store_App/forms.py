from django.contrib.auth.forms import UserCreationForm

from Web_Store.Store_App.models import CustomerUser


class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomerUser
        fields = ('username', 'email')
