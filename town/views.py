from django.shortcuts import render
from .models import Town, Shop, Item


def town_list(request):
    towns = Town.objects.all()
    return render(request, 'town/town_list.html', {'towns': towns})


def town_detail(request, pk):
    town = Town.objects.get(pk=pk)
    shops = Shop.objects.filter(area=town)
    params = {
        'town': town,
        'shops': shops,
    }
    return render(request, 'town/town_detail.html', params)


def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)

    params = {
        'shop': shop
    }
    return render(request, 'shop/shop_detail.html', params)


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)

    params = {
        'item': item
    }
    return render(request, 'item/item_detail.html', params)
