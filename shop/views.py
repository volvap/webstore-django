from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItem, Order
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from datetime import datetime


CACHE_TTL = 60 * 20


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item_list.html", context)


@login_required(login_url='/log')
def add_to_cart(request,pk):
    item = get_object_or_404(Item, pk=pk)
    order_item = OrderItem.objects.create(item=item)
    if Order.objects.filter(user=request.user).exists():
        user_order = Order.objects.get(user=request.user)
        user_order.items.add(order_item)
        user_order.save()
    else:
        user_order = Order.objects.create(user=request.user, ordered_date=datetime.now())
        user_order.items.add(order_item)
    user_order.save()

    context = {
        "order": order_item
    }
    return render(request, 'add_to_cart.html', context)


def delete_all_from_cart(request):
    order_items = OrderItem.objects.filter().delete()
    context = {
        'items': Item.objects.all()
    }
    return render(request, "cart.html", context)


@login_required(login_url='/log')
def display_cart(request):
    order = Order.objects.filter(user=request.user).latest('ordered_date')
    context = {
        'order_items': order.items
    }
    return render(request, "cart.html", context)
