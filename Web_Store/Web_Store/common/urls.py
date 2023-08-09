from django.urls import path

from Web_Store.common import views

urlpatterns = (
    path('', views.store_view, name='store'),
    path('cart/<int:pk>/', views.cart_view, name='cart'),

)
