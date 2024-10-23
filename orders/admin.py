from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'user', 'is_active', 'order_date']
    inlines = [
        OrderProductInlineAdmin,
    ]
    # list_filter = ['is_active', 'order_date']
    # search_fields = ['user__username', 'user__email']
    # list_editable = ['is_active']
    # date_hierarchy = 'order_date'
    # readonly_fields = ['order_date']

admin.site.register(Order, OrderAdmin)


# class OrderProductAdmin(admin.ModelAdmin):
#     list_display = ['order', 'product', 'quantity']
#     list_filter = ['product']
#     search_fields = ['product__name']
#     list_editable = ['quantity']