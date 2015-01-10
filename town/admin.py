from django.contrib import admin
from .models import Town, Shop, Item, Stock, Order, OrderItem, OrderStatus
# Register your models here.
admin.site.register(Town)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderStatus)
