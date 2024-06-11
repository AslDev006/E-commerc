from django.db import models
from users.models import *
from warehouse.models import *
from products.models import *

class MainComment(models.Model):
    STATUS = (
        (active, active),
        (deactive, deactive),

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    warehouse_product = models.ForeignKey(WareHouseProduct, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUS, default=active)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class SubComment(models.Model):
    STATUS = (
        (active, active),
        (deactive, deactive),
    )

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(MainComment, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUS, default=active)



class productLike(models.Model):
    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    warehouse_product = models.ForeignKey(WareHouseProduct, on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class CommentLike(models.Model):
    like = models.BooleanField(default=False)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(MainComment, on_delete=models.CASCADE)



class SubCommentLike(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(SubComment, on_delete=models.CASCADE)