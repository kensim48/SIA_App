from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from vendor.models import Store
from orders.models import Order, OrderMeal, OrderDetails

STORE_ID = 1


class OrderList(APIView):
    def get(self, request):
        store = Store.objects.get(store_ID=STORE_ID)
        orders = Order.objects.filter(store=store, status=1)
        order_list = []
        for order in orders:
            # status 1 means havent been cooked
            order_meals = OrderMeal.objects.filter(order=order)
            meal_list = []
            for order_meal in order_meals:
                order_details = OrderDetails.objects.filter(meal=order_meal)
                order_detail_list = []
                for order_detail in order_details:
                    order_detail_list.append(order_detail.detail)
                meal_list.append({"foodTitle": order_meal.title,
                                  "foodDescription": order_detail_list})
            order_list.append({"orderNum": order.name,
                               "meals": meal_list})
        print(order_list)
        return Response({"orders": order_list})


class ClearOrder(APIView):
    def post(self, request):
        order_hash = json.loads(request.body)['orderHash']
        order_meal = OrderMeal.objects.get(order_hash=order_hash)
        order_meal.status = 0
        order_meal.save()
        return Response("done")
