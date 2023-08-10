from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from Web_Store.accounts.models import CustomerUser
from Web_Store.accounts.forms import CustomerUserCreationForm, LoginForm, CustomerUserEditForm

from django.contrib.auth import views as auth_views

from Web_Store.common.models import Order


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


@login_required
def get_profile_details(request, pk):
    profile = request.user
    orders = Order.objects.filter(customer=profile, complete=True)
    context = {
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'profile/details-page.html', context)


@login_required
def delete_profile(request, pk):
    user = get_object_or_404(CustomerUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('store')

    return render(request, 'profile/delete-page.html', {'user': user})


class UserEditView(generic.UpdateView):
    model = CustomerUser
    form_class = CustomerUserEditForm
    template_name = 'profile/edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})
