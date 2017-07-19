from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..admin_app.models import Admins
from .models import Products
import bcrypt

def get_all_products():
  return Products.objects.all()

def get_product_by_id(id):
  return Products.objects.get(id = id)

def filter_product_by_id(id):
  return Products.objects.filter(id = id)

def add_product(name, dept, style, design, material, price, cost):
  Products.objects.create(name = name, dept = dept, style = style, design = design, material = material, price = price, cost = cost)
  return 'Donesky'

def delete_product(id):
  print 'Deleting product with id: ' + str(id)
  Products.objects.get(id = id).delete()
  return 'Done-zo'

# Create your views here.

def index(request):
  print 'IT\'S WORKING'
  products = get_all_products()
  context = {
    'products' : products
  }
  return render(request, 'manage_products/index.html', context)

def add_product_page(request):
  return render(request, 'manage_products/add_product.html')

def add_product_to_db(request):
  print "It's working! It's working!"
  name = request.POST['name']
  dept = request.POST['dept']
  style = request.POST['style']
  design = request.POST['design']
  material = request.POST['material']
  price = request.POST['price']
  cost = request.POST['cost']
  print 'name: ' + name
  print 'dept: ' + dept
  print 'style: ' + style
  print 'design: ' + design
  print 'material: ' + material
  print 'price: ' + price
  print 'cost: ' + cost
  print add_product(name, dept, style, design, material, price, cost)
  return redirect(reverse('manage_products_index'))

def edit_product_page(request, id):
  products = filter_product_by_id(id)
  print products[0].name
  context = {
    'products' : products
  }
  return render(request, 'manage_products/edit_product.html', context)

def edit_product(request):
  id = request.POST['id']
  name = request.POST['name']
  dept = request.POST['dept']
  style = request.POST['style']
  design = request.POST['design']
  material = request.POST['material']
  price = request.POST['price']
  cost = request.POST['cost']
  product = get_product_by_id(id)
  product.name = name
  product.dept = dept
  product.style = style
  product.design = design
  product.material = material
  product.price = price
  product.cost = cost
  product.save()
  return redirect(reverse('manage_products_index'))

def delete_product_from_db(request):
  id = request.POST['id']
  print 'product id: ' + str(id)
  print delete_product(id)
  return redirect(reverse('manage_products_index'))