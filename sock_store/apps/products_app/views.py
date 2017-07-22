from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..manage_products.models import Products
import bcrypt
from django.contrib.auth import authenticate, login

def index(request):
    # del request.session['cart']
    products = Products.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'products_app/index.html', context)

def sale(request):
    return render(request, 'products_app/sale.html')

def womens(request):
    return render(request, 'products_app/womens.html')

def mens(request):
    return render(request, 'products_app/mens.html')

def girls(request):
    return render(request, 'products_app/girls.html')

def boys(request):
    return render(request, 'products_app/boys.html')

def product(request, id):
    print 'MEOW'
    product = Products.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'products_app/product.html', context)

def cart(request):
    print 'CART PAGE'
    cart_items = []
    total = 0
    if 'cart' in request.session:
        cart = request.session['cart']
        for key in cart:
            print '***********MIKE SUCKS'
            print 'quantity ' + request.session['cart'][key]
            print key
            print type(key)
            cart_item = Products.objects.get(id= int(key))
            cart_items.append(cart_item)
            total_price = cart_item.price*int(cart[key])
            print cart[key]
            print total_price
            total += int(total_price)
    context = {
        'cart_items' : cart_items,
        'total' : total
    }
    return render(request, 'products_app/cart.html', context)

def add_to_cart(request):
    print 'adding to cart'
    id = request.POST['id']
    key = str(id)
    cart = request.session['cart']
    cart[key] = id
    request.session['cart'] = cart
    return redirect(reverse('products_main'))