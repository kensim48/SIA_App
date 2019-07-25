from django.db import models
import os
from binascii import hexlify

def _createId():
    return str(hexlify(os.urandom(16)))[2:34]

# Create your models here.


class Store(models.Model):
    store_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


# add unique hash for meal
class Meal(models.Model):
    meal_ID = models.AutoField(primary_key=True)
    meal_hash = models.CharField(max_length=32, default=_createId)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    meal_owner = models.ForeignKey(Store, default=None, on_delete=models.CASCADE)


class Question(models.Model):
    question_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.IntegerField()
    option_limit_lower = models.IntegerField()
    option_limit_upper = models.IntegerField()
    meal = models.ForeignKey(Meal, default=None, on_delete=models.CASCADE)


class Option(models.Model):
    option_ID = models.AutoField(primary_key=True)
    option_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, default=None, on_delete=models.CASCADE)