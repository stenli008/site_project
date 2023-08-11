from Web_Store.common.models import *
from django.contrib import admin

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Order)

admin.site.register(Shipping)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added', 'get_total')
    list_filter = ('order', 'product')
    search_fields = ('product__name', 'order__id')
    ordering = ('-date_added',)
    actions = ['mark_as_processed']


admin.site.register(OrderItem, OrderItemAdmin)
