from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Web_Store.common.models import Product, Order
from Web_Store.accounts.models import CustomerUser


def store_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'core/store.html', context)


@login_required
def cart_view(request, pk):
    customer = CustomerUser.objects.get(pk=pk)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    context = {
        'customer': customer,
        'order': order,
        'items': items,
    }
    return render(request, 'core/cart.html', context)
