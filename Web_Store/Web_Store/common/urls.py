from django.urls import path, include
from Web_Store.common import views

urlpatterns = (
    path('', views.store_view, name='store'),
    path('category/<int:category_id>/', views.store_view, name='store_by_category'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('product/<int:pk>', views.product_view, name='product'),
    path('cancel_order/<int:order_id>', views.cancel_order, name='cancel_order'),
    path('update_quantity/<int:item_id>', views.update_quantity, name='update_quantity'),
    path('cart/<str:username>/', include([
        path('', views.cart_view, name='cart'),
        path('checkout/', views.checkout, name='checkout'),
    ])),

)
