from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..admin_app.models import Admins
from .models import Products, Sizes, Product_Sizes

def get_all_products():
  return Products.objects.all()

def get_product_by_id(id):
  return Products.objects.get(id = id)

def filter_product_by_id(id):
  return Products.objects.filter(id = id)

def add_product(name, dept, style, design, material, price, cost, image):
  return Products.objects.create(name = name, dept = dept, style = style, design = design, material = material, price = price, cost = cost, image = image)

def delete_product(id):
  print 'Deleting product with id: ' + str(id)
  Products.objects.get(id = id).delete()
  return 'Done-zo'

def link_size_to_product(size_id, product_id):
  print 'LINKING SIZE TO PRODUCT'
  size = Sizes.objects.get(id = size_id)
  product = Products.objects.get(id = product_id)
  print size.size
  print product.name
  Product_Sizes.objects.create(size = size, product = product)
  return 'Done-zo'

# Create your views here.

def index(request):
  print 'IT\'S WORKING'
  products = get_all_products()
  sizes = Sizes.objects.all()
  for size in sizes:
    print size.size
    print size.product_sizes
    for relationship in size.product_sizes.all():
      print relationship
  product_sizes = Product_Sizes.objects.all()
  product_sizes = Product_Sizes.objects.all()
  for relationship in product_sizes:
    print relationship.product.name + ':' + relationship.size.size
  # print sizes[0].products
  # print products[0].sizes
  context = {
    'products' : products
  }
  return render(request, 'manage_products/index.html', context)

def add_product_page(request):
  sizes = Sizes.objects.all()
  for size in sizes:
    print str(size.id) + ': ' + size.size
  context = {
    'sizes' : sizes
  }
  return render(request, 'manage_products/add_product.html', context)

def add_product_to_db(request):
  print "It's working! It's working!"
  name = request.POST['name']
  dept = request.POST['dept']
  style = request.POST['style']
  design = request.POST['design']
  material = request.POST['material']
  price = request.POST['price']
  cost = request.POST['cost']
  image = request.POST['image']
  print 'name: ' + name
  print 'dept: ' + dept
  print 'style: ' + style
  print 'design: ' + design
  print 'material: ' + material
  print 'price: ' + price
  print 'cost: ' + cost
  product = add_product(name, dept, style, design, material, price, cost, image)
  if 'size_1' in request.POST:
    size_id = int(request.POST['size_1'])
    link_size_to_product(size_id, product.id)
  if 'size_2' in request.POST:
    size_id = int(request.POST['size_2'])
    link_size_to_product(size_id, product.id)
  if 'size_3' in request.POST:
    size_id = int(request.POST['size_3'])
    link_size_to_product(size_id, product.id)
  if 'size_4' in request.POST:
    size_id = int(request.POST['size_4'])
    link_size_to_product(size_id, product.id)
  if 'size_5' in request.POST:
    size_id = int(request.POST['size_5'])
    link_size_to_product(size_id, product.id)
  if 'size_6' in request.POST:
    size_id = int(request.POST['size_6'])
    link_size_to_product(size_id, product.id)
  if 'size_7' in request.POST:
    size_id = int(request.POST['size_7'])
    link_size_to_product(size_id, product.id)
  if 'size_8' in request.POST:
    size_id = int(request.POST['size_8'])
    link_size_to_product(size_id, product.id)
  if 'size_9' in request.POST:
    size_id = int(request.POST['size_9'])
    link_size_to_product(size_id, product.id)
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
  image = request.POST['image']
  product = get_product_by_id(id)
  product.name = name
  product.dept = dept
  product.style = style
  product.design = design
  product.material = material
  product.price = price
  product.cost = cost
  product.image = image
  product.save()
  return redirect(reverse('manage_products_index'))

def delete_product_from_db(request):
  id = request.POST['id']
  print 'product id: ' + str(id)
  print delete_product(id)
  return redirect(reverse('manage_products_index'))