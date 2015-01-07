from django.shortcuts import render
from .models import Town


def town_list(request):
    towns = Town.objects.all()
    return render(request, 'town/town_list.html', {'towns': towns})
