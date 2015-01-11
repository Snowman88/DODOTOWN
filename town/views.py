from django.shortcuts import render, redirect
from django.http import Http404
from .models import Town, Shop, Item, Cart, CartItem


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


def cart_add(request):
    if request.method == 'POST':
        # cart がないなら作成
        cart, cart_created = Cart.objects.get_or_create(
            customer=request.user)
        item_id = request.POST.get("item_id", 0)
        item = Item.objects.get(pk=item_id)
        quantity = 1
        try:
            cart_item = CartItem.objects.get(item=item)
            cart_item.quantity += quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem(cart=cart, item=item, quantity=quantity)
            cart_item.save()

        return redirect('town.views.item_detail', pk=item_id)
    else:
        raise Http404
