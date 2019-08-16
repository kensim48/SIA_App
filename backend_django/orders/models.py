from django.db import models
import os
from binascii import hexlify
from vendor.models import Store


def _createIdOrder():
    return str(hexlify(os.urandom(16)))[2:34]
# Create your models here.


class Order(models.Model):
    order_hash = models.CharField(primary_key=True, max_length=32, default=_createIdOrder)
    status = models.SmallIntegerField(default=1)
    store = models.ForeignKey(Store, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


# add unique hash for meal
class OrderMeal(models.Model):
    title = models.CharField(max_length=255)
    order = models.ForeignKey(Order, default=None, on_delete=models.CASCADE)


class OrderDetails(models.Model):
    detail = models.CharField(max_length=255)
    meal = models.ForeignKey(OrderMeal, default=None, on_delete=models.CASCADE)
