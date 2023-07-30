from django.contrib import admin

from StoreFront.Store_App.models import Product, ProductCategory, Customer, Order, OrderItem

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
