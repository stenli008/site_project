from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from Web_Store.common.models import Product, Order, OrderItem
from Web_Store.accounts.models import CustomerUser


def store_view(request):
    products = Product.objects.all()
    user = request.user
    context = {
        'products': products,
        'user': user,
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


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, item_created = OrderItem.objects.get_or_create(product=product, order=order)

    if not item_created:
        order_item.quantity += 1
    else:
        order_item.quantity += 1

    order_item.save()

    return redirect('store')


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
    }

    return render(request, 'core/product_page.html', context)
