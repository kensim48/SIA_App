from django.db import models
import os
from binascii import hexlify

def _createIdMeal():
    return str(hexlify(os.urandom(16)))[2:34]
def _createIdQuestion():
    return str(hexlify(os.urandom(16)))[2:34]
def _createIdOption():
    return str(hexlify(os.urandom(16)))[2:34]

# Create your models here.


class Store(models.Model):
    store_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


# add unique hash for meal
class Meal(models.Model):
    meal_hash = models.CharField(primary_key=True, max_length=32, default=_createIdMeal)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    meal_owner = models.ForeignKey(Store, default=None, on_delete=models.CASCADE)


class Question(models.Model):
    question_hash = models.CharField(primary_key=True, max_length=32, default=_createIdQuestion)
    title = models.CharField(max_length=255)
    type = models.IntegerField()
    option_limit_lower = models.IntegerField(null=True)
    option_limit_upper = models.IntegerField(null=True)
    meal = models.ForeignKey(Meal, default=None, on_delete=models.CASCADE)


class Option(models.Model):
    option_hash = models.CharField(primary_key=True, max_length=32, default=_createIdOption)
    option_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, default=None, on_delete=models.CASCADE)