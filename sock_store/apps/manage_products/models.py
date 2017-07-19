from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Products(models.Model):
  name = models.CharField(max_length = 255)
  dept = models.CharField(max_length = 255)
  style = models.CharField(max_length = 255)
  design = models.CharField(max_length = 255)
  material = models.CharField(max_length = 255)
  price = models.IntegerField()
  cost = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)