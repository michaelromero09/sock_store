from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..manage_products.models import Products

# Create your views here.
def index(request):
    cart_items = []
    total = 0
    order_total = total + 5
    if 'cart' in request.session:
        cart = request.session['cart']
        for key in cart:
            print '***********MIKE SUCKS'
            print 'quantity ' + request.session['cart'][key]
            print key
            print type(key)
            cart_item = Products.objects.get(id= int(key))
            cart_items.append(cart_item)
            total_price = cart_item.price*int(cart[key]) #should be multiplied by the quantity, NOT the bloody ID. But I have no idear what I'm doin'.
            print cart[key]
            print total_price
            total += int(total_price)
    context = {
        'cart_items' : cart_items,
        'total' : total,
        'order_total' : order_total
    }
    return render(request, 'checkout/index.html', context)