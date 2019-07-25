from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from vendor.models import Store, Meal, Question, Option


class MenuItems(APIView):
    def get(self, request):
        STORE_ID = 1
        store = Store.objects.get(store_ID=STORE_ID)
        meals = Meal.objects.filter(meal_owner=store)
        meal_list = []
        for meal in meals:
            questions = Question.objects.filter(meal=meal)
            question_list = []
            single_question ={}
            for question in questions:
                options = Option.objects.filter(question=question)
                option_list = []
                for option in options:
                    option_list.append(option)
                single_question = {"type": question.type,
                                  "optionLimits": [question.option_limit_lower, question.option_limit_upper],
                                  "title": question.title, "options": option_list}
                question_list.append(single_question)

            single_meal = {
                "title": meal.title,
                "mealID": meal.meal_ID,
                "description": meal.description,
                "price": meal.price,
                "questions": question_list
            }
            print(question_list)
            meal_list.append(single_meal)

        single_store = {
            "storeName": store.name,
            "menuItems": meal_list
        }
        return Response(single_store)

    def post(self, request):
        data = json.loads(request.body)['menuItems']
        data = json.loads(request.body)['storeName']
        print(data)
        STORE_ID = 1
        store = Store.objects.get(store_ID=STORE_ID)
        meals = Meal.objects.filter(meal_owner=store)
        meal_list = []
        for meal in meals:
            questions = Question.objects.filter(meal=meal)
            question_list = []
            single_question = {}
            for question in questions:
                options = Option.objects.filter(question=question)
                option_list = []
                for option in options:
                    option_list.append(option)
                single_question = {"type": question.type,
                                   "optionLimits": [question.option_limit_lower, question.option_limit_upper],
                                   "title": question.title, "options": option_list}
                question_list.append(single_question)

            single_meal = {
                "mealID": meal.meal_ID,
                "title": meal.title,
                "description": meal.description,
                "price": meal.price,
                "questions": question_list
            }
            print(question_list)
            meal_list.append(single_meal)

        single_store = {
            "storeName": store.name,
            "menuItems": meal_list
        }
        return Response(single_store)



        # airplanes = Airplane.objects.order_by("item_number")
        # full_list = []
        # for i in airplanes:
        #     full_list.append(
        #         {
        #             'itemno': i.item_number,
        #             'partno': i.part_number,
        #             'description': i.description,
        #             'ipc': i.ipc_ref,
        #             'qty': i.quantity
        #         }
        #     )
        # return Response(full_list)

class singleMeal(APIView):

    def post(self):
        pass
