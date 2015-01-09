from django.contrib import admin
from .models import Town, Shop, Item, Stock
# Register your models here.
admin.site.register(Town)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Stock)
