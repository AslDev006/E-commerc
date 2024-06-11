from django.db import models

from users.models import *

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale = models.DecimalField(max_digits=20, decimal_places=2)
    cost_of_entry = models.DecimalField(max_digits=20, decimal_places=2)
    income = models.DecimalField(max_digits=20, decimal_places=2)
    total_count = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('MainCategory', on_delete=models.CASCADE)


class MainCategory(models.Model):
    name = models.CharField(max_length=255)
    # subcategory = models.ForeignKey('MainCategory')


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)


class Features(models.Model):
    STATUS = (
        ('active', active),
        ('deactive', deactive)

    )
    image = models.ImageField(upload_to="product_images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')
    size_type = models.CharField(max_length=25)
    size = models.IntegerField(null=True, blank=True)
    colour = models.CharField(max_length=24)
    count = models.IntegerField()
    status = models.CharField(max_length=30, choices=STATUS, default=deactive)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
