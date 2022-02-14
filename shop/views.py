from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, OrderUpdate
from math import ceil
import json


# Create your views here.


def index(request):
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allproducts': allProds}
    return render(request, "shop/index.html", params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod_temp = Product.objects.filter(category=cat)
        prod = [item for item in prod_temp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if n != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allproducts': allProds}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id', '')
        phone = request.POST.get('phone', '')
        try:
            order = Order.objects.filter(order_id=order_id, phone=phone)
            print(order, list(order))
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    desc = item.get_update_desc_display()
                    updates.append(
                        {'desc': desc, 'time': item.timestamp})
                    response = json.dumps(
                        [updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception:
            return HttpResponse('{}')
    return render(request, "shop/tracker.html")


def products(request, pid):
    prod = Product.objects.filter(id=pid)[0]
    return render(request, "shop/prodview.html", {'product': prod})


def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        total_amount = request.POST.get('total_amount', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('addressline1', '') + " , " + \
            request.POST.get('addressline2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')

        order = Order(items_json=itemsJson, total_amount=total_amount, name=name, email=email, phone=phone,
                      address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        confirm = True
        id = order.order_id
        update = OrderUpdate(order_id=id)
        update.save()

        return render(request, 'shop/checkout.html', {"confirm": confirm, "id": id})

    return render(request, "shop/checkout.html")
