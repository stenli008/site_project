from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from Web_Store.Store_App.models import CustomerUser
from Web_Store.Store_App.forms import CustomerUserCreationForm


def store_view(request):
    return render(request, 'core/store.html')


class UserRegisterView(generic.CreateView):
    model = CustomerUser
    form_class = CustomerUserCreationForm
    template_name = 'profile/register.html'
    success_url = reverse_lazy('login')
