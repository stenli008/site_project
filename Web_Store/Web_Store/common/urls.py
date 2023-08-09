from django.urls import path

from Web_Store.common import views

urlpatterns = (
    path('', views.store_view, name='store'),
    path('cart/<int:pk>/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('product/<int:pk>', views.product_view, name='product')

)
