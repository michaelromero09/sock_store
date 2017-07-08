from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Admins
import bcrypt

# Create your views here.
def index(request):
  return render(request, 'admin_app/index.html')

def login(request):
  email = request.POST['email']
  errors = Admins.objects.login_validator(request.POST)
  if len(errors):
    for tag,error in errors.iteritems():
      messages.add_message(request, messages.ERROR, str(error))
    return redirect('/admin')
  else:
    request.session['id'] = Admins.objects.get(email = email).id
    #messages.add_message(request, messages.SUCCESS, "Successfully logged in!")
    return redirect('/mission_control')

def register(request):
  email = request.POST['email']
  password = request.POST['password']
  confirm_pw = request.POST['confirm_pw']
  salt=bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(request.POST['password'].encode(encoding='utf-8', errors='strict'), salt)
  errors = Admins.objects.register_validator(request.POST)
  print errors
  if len(errors):
    for tag,error in errors.iteritems():
      messages.add_message(request, messages.ERROR, str(error))
      return redirect('/admin')
  else: 
    admin = Admins.objects.create(email = email, password = hashed_password)
    messages.add_message(request, messages.SUCCESS, "Successfully registered!")
    request.session['id'] = Admins.objects.get(email = email).id
    print ('*'*50)
    print Admins.objects.all()
    return redirect('/mission_control')

def mission_control(request):
  return render(request, 'admin_app/mission_control.html')

def logout(request):
  del request.session['id']
  return redirect('/admin')