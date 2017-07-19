from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^submit_registration$', views.submit_registration),
    url(r'^login_user$', views.login_user),
    url(r'^subscribe$', views.subscribe),
    url(r'^about$', views.about),
    url(r'^products$', views.products),
    url(r'^products/sale$', views.sale),
    url(r'^cart$', views.cart),
    url(r'^contact$', views.contact),
]