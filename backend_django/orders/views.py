from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from vendor.models import Store
from orders.models import Order, OrderMeal, OrderDetails

STORE_ID = 1


class MenuItems(APIView):
    def get(self, request):
        store = Store.objects.get(store_ID=STORE_ID)
        orders = Order.objects.filter(store=store)
        for order in orders:
            order_meals = OrderMeal.objects.filter(order=order, status=1)
            for order_meal in order_meals:
                order_details = OrderDetails.objects.filter(meal=order_meal)
                order_detail_list = []
                for order_detail in order_details:
                    order_detail_list.append(order_detail.detail)

        meals = Meal.objects.filter(meal_owner=store)
        meal_list = []
        for meal in meals:
            questions = Question.objects.filter(meal=meal)
            question_list = []
            for question in questions:
                options = Option.objects.filter(question=question)
                option_list = []
                for option in options:
                    option_list.append(option.option_text)
                single_question = {"type": question.type,
                                   "optionLimits": [question.option_limit_lower, question.option_limit_upper],
                                   "title": question.title, "options": option_list}
                question_list.append(single_question)

            single_meal = {
                "title": meal.title,
                "description": meal.description,
                "price": meal.price,
                "questions": question_list,
                "meal_hash": meal.meal_hash,
                "store_ID": meal.meal_owner.store_ID
            }
            meal_list.append(single_meal)

        single_store = {
            "storeName": store.name,
            "menuItems": meal_list,
            "storeID":  store.store_ID
        }
        return Response(single_store)