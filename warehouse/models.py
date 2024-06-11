from django.db import models
from users.models import *
from products.models import *


class WareHouseProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    size_type = models.CharField(max_length=25)
    size = models.IntegerField()
    warehouse  = models.ForeignKey('WareHouse', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class WareHouse(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('TYPE', on_delete=models.CASCADE)


class TYPE(models.Model):
    name = models.CharField(max_length=255)

class WarehouseCorporation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    warehouse_id = models.ForeignKey(WareHouse, on_delete=models.CASCADE)