from django.contrib import admin
from orders.models import Order, OrderMeal, OrderDetails


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_hash', 'store', 'name')
    ordering = ['order_hash']


class OrderMealAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ['order']


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('detail', 'meal')
    ordering = ['meal']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderMeal, OrderMealAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
