from django.urls import reverse_lazy
from django.views import generic

from Web_Store.accounts.models import CustomerUser
from Web_Store.accounts.forms import CustomerUserCreationForm, LoginForm

from django.contrib.auth import views as auth_views


class UserRegisterView(generic.CreateView):
    model = CustomerUser
    form_class = CustomerUserCreationForm
    template_name = 'profile/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'profile/login-page.html'
    next_page = reverse_lazy('store')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')
