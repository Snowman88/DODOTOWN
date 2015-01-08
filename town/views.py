from django.shortcuts import render
from .models import Town, Shop


def town_list(request):
    towns = Town.objects.all()
    return render(request, 'town/town_list.html', {'towns': towns})


def town_detail(request, pk):
    town = Town.objects.get(pk=pk)
    shops = Shop.objects.all()
    params = {
        'town': town,
        'shops': shops,
    }
    return render(request, 'town/town_detail.html', params)
