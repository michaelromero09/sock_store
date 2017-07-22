from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ='products_main'),
    url(r'^sale$', views.sale, name ='products_sale'),
    url(r'^womens$', views.womens, name ='products_womens'),
    url(r'^mens$', views.mens, name ='products_mens'),
    url(r'^girls$', views.girls, name ='products_girls'),
    url(r'^boys$', views.boys, name ='products_boys'),
    url(r'^product/(?P<id>\d+)$', views.product, name ='product'),
    url(r'^cart$', views.cart, name ='cart'),
    url(r'^add_to_cart$', views.add_to_cart, name ='add_to_cart'),
]
    