from django.contrib import admin

from .models import Order, OrderItem



# class OrderAdmin(admin.TabularInline):
#     model = Order

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'paid_amount', 'status']
    inlines =  [OrderItemAdmin]


admin.site.register(Order, OrderAdmin)
#admin.site.register(OrderItem)