from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^mission_control$', views.mission_control),
    url(r'^logout$', views.logout),
]