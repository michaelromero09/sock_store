from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users, Addresses
import bcrypt
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'store_app/index.html')

def register(request):
    return render(request, 'store_app/register.html')

def submit_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_num = request.POST['phone_num']
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(encoding='utf-8', errors='strict'), salt)
        confirm_pw = request.POST['confirm_pw']
        name = request.POST['name']
        street = request.POST['street']
        street2 = request.POST['street2']
        city = request.POST['city']
        state = str(request.POST['state'])
        zip_code = request.POST['zip_code']
        user_errors = Users.objects.user_validator(request.POST)
        address_errors = Addresses.objects.address_validator(request.POST)
        if len(user_errors) or len(address_errors):
            for tag,user_error in user_errors.iteritems():
                messages.add_message(request, messages.ERROR, str(user_error))
            for tag,address_error in address_errors.iteritems():
                messages.add_message(request, messages.ERROR, str(address_error))
            return redirect('/register')
        else: 
            user = Users.objects.create(first_name = first_name, last_name = last_name, email = email, phone_num = phone_num, password = hashed_password)
            address = Addresses.objects.create(name = name, street = street, street2 = street2, city = city, state = state, zip_code = zip_code )
            messages.add_message(request, messages.SUCCESS, "Successfully registered and logged in!")
            request.session['id'] = Users.objects.get(email = email).id
            print 'success!!!!'
            return redirect('/')

def login_user(request):
    email = request.POST['email']
    password = request.POST['password']
    #Return an 'invalid login' error message.
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.add_message(request, messages.ERROR, str(error))
        return redirect('/')
    else:
        request.session['id'] = Users.objects.get(email = email).id
        messages.add_message(request, messages.SUCCESS, "Successfully logged in!")
        return redirect('/')

def logout(request):
    del request.session['id']
    return redirect ('/')

def subscribe(request):
    return redirect('/')

def about(request):
    return render(request, 'store_app/about.html')

def products(request):
    return render(request, 'store_app/products.html')

def sale(request):
    return render(request, 'store_app/sale.html')

def cart(request):
    return render(request, 'store_app/cart.html')

def contact(request):
    return render(request, 'store_app/contact.html')
