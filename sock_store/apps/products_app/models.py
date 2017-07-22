from __future__ import unicode_literals

from django.db import models

# Do I even want to do this????
# class Carts(models.Model):
#     item_count = models.IntegerField(default='')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Cart_Items(models.Model):
#     item_name = models.CharField(max_length=100)
#     quantity = models.IntegerField(default='')
#     item_price = models.IntegerField(default='')
#     cart = models.ForeignKey(Carts, related_name='cart_items')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Orders(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=255)
#     phone_num = models.IntegerField(default='')
#     password = models.CharField(max_length=50)
#     confirm_pw = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)