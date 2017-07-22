from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..manage_products.models import Products
from ..store_app.models import Users
# from . models import Carts, Cart_Items
import bcrypt
from django.contrib.auth import authenticate, login

def index(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    if 'id' in request.session:
        products = Products.objects.all()
        user = Users.objects.get(id= request.session['id'])
        context = {
            'user' : user,
            'products' : products
        }
        return render(request, 'products_app/index.html', context)
    return render(request, 'products_app/index.html', context)

def sale(request):
    if 'id' in request.session:
        user = Users.objects.get(id= request.session['id'])
        context = {
            'user' : user
        }
        return render(request, 'store_app/index.html', context)
    else: 
        return render(request, 'store_app/index.html')

    return render(request, 'products_app/sale.html')

def womens(request):
    if 'id' in request.session:
        user = Users.objects.get(id= request.session['id'])
        context = {
            'user' : user
        }
        return render(request, 'store_app/index.html', context)
    else: 
        return render(request, 'store_app/index.html')

    return render(request, 'products_app/womens.html')

def mens(request):
    if 'id' in request.session:
        user = Users.objects.get(id= request.session['id'])
        context = {
            'user' : user
        }
        return render(request, 'store_app/index.html', context)
    else: 
        return render(request, 'store_app/index.html')

    return render(request, 'products_app/mens.html')

def girls(request):
    if 'id' in request.session:
        user = Users.objects.get(id= request.session['id'])
        context = {
            'user' : user
        }
        return render(request, 'store_app/index.html', context)
    else: 
        return render(request, 'store_app/index.html')

    return render(request, 'products_app/girls.html')

def boys(request):
    if 'id' in request.session:
        user = Users.objects.get(id= request.session['id'])
        context = {
            'user' : user
        }
        return render(request, 'store_app/index.html', context)
    else: 
        return render(request, 'store_app/index.html')

    return render(request, 'products_app/boys.html')

def product(request, id):
    if 'id' in request.session:
        user = Users.objects.get(id= request.session['id'])
        context = {
            'user' : user
        }
        return render(request, 'store_app/index.html', context)
    else: 
        return render(request, 'store_app/index.html')

    print 'MEOW'
    product = Products.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'products_app/product.html', context)

def cart(request):
    if 'id' in request.session:
        user = Users.objects.get(id= request.session['id'])
        cart_is_empty = True
        print 'CART PAGE'
        cart_items = []
        total = 0
        item_total = 0
        order_total = 0
        shipping = 5
        cart = request.session['cart']
        if cart != {}:
            for key in cart:
                cart_is_empty = False
                print '***********MIKE SUCKS'
                cart_item = Products.objects.get(id= int(key))
                cart_items.append(cart_item)
                quantity = cart[key]
                print quantity
                total_price = cart_item.price*int(quantity) 
                print cart[key]
                print total_price
                total += int(total_price)
                order_total = total + shipping
                item_total += quantity
                print item_total
            context = {
                'cart_items' : cart_items,
                'total' : total,
                'order_total' : order_total,
                'user' : user,
                'quantity' : quantity,
                'cart_is_empty' : cart_is_empty,
                'item_total' : item_total
            }
        else: 
            context = {
                'cart_is_empty' : cart_is_empty
            }
        return render(request, 'products_app/cart.html', context)


def add_to_cart(request):
    cart = request.session['cart']
    id = request.POST['id']
    key = str(id)
    if key in cart:
        cart[key] = int(cart[key]) +1
        request.session['cart'] = cart
    if key not in cart:
        print 'adding to cart'
        cart[key] = 1
        print 'key: ' + key
        print 'cart[key]: ' + str(cart[key])
        request.session['cart'] = cart
    return redirect(reverse('products_main'))