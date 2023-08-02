from django.contrib import admin

from StoreFront.Store_App.models import Product, ProductCategory, Customer, OrderStatus, OrderItem, Order

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Customer)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(OrderItem)



