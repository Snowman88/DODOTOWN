from django.db import models
from django.utils import timezone


class Town(models.Model):
    name = models.CharField(max_length=200, verbose_name="Town")
    size = models.IntegerField()
    address = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="住所")
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Shop(models.Model):
    owner = models.ForeignKey('auth.User', verbose_name="所有者")
    area = models.ForeignKey('Town', verbose_name="所属の町")
    name = models.CharField(max_length=255, verbose_name="Shop")
    description = models.TextField(null=True, blank=True, verbose_name="商品説明")
    size = models.IntegerField()
    address = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="住所")
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="商品名")
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True, verbose_name="商品説明")
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Stock(models.Model):
    shop = models.ForeignKey('Shop')
    item = models.OneToOneField('Item')
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} * {}".format(self.item.name, self.quantity)


class Order(models.Model):
    customer = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Ordered at {}".format(self.created.strftime("%Y-%m-%d %H:%m:%s"))


class OrderItem(models.Model):
    order = models.ForeignKey('Order')
    item = models.ForeignKey('Item')
    quantity = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name


class OrderStatus(models.Model):
    CART_STATUS = 0
    DEAL_STATUS = 1
    STATUS_CHOICES = (
        (CART_STATUS, 'Cart'),
        (DEAL_STATUS, 'Deal'),
    )

    order = models.OneToOneField('Order')
    status = models.IntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
