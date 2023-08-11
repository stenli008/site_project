from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from Web_Store.common.forms import ShippingForm
from Web_Store.common.models import Product, Order, OrderItem, ProductCategory
from Web_Store.accounts.models import CustomerUser


def store_view(request, category_id=None):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    if category_id:
        selected_category = ProductCategory.objects.get(id=category_id)
        products = products.filter(category=selected_category)
    user = request.user
    context = {
        'products': products,
        'user': user,
        'categories': categories,
    }
    return render(request, 'core/store.html', context)


@login_required
def cart_view(request, username):
    customer = get_object_or_404(CustomerUser, username=username)
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


def checkout(request, username):
    customer = CustomerUser.objects.get(username=username)
    order = Order.objects.filter(customer=customer, complete=False).first()
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.customer = customer
            shipping.order = order
            shipping.save()

            order.complete = True
            order.save()

            return redirect('profile-details', customer.pk)
    else:
        form = ShippingForm()

    context = {
        'form': form,
        'order': order,
    }

    return render(request, 'core/checkout.html', context)


def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    user = request.user
    context = {
        'order': order,
        'user': user,
    }
    if request.method == 'POST':
        order.status = 'Canceled'
        order.save()

        return redirect('profile-details', pk=order.customer.pk)

    return render(request, 'core/cancel_order.html', context)


def update_quantity(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    user = request.user
    if request.method == 'POST':
        action = request.POST.get('action')
        quantity = int(item.quantity)

        if action == 'increment':
            quantity += 1
            item.quantity = quantity
            item.save()
        elif action == 'decrement':
            quantity -= 1
            if quantity < 1:
                item.delete()
            else:
                item.quantity = quantity
                item.save()

    return redirect('cart', username=user.username)
