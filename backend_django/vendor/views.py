from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from vendor.models import Store, Meal, Question, Option

STORE_ID = 1


class MenuItems(APIView):
    def get(self, request):

        store = Store.objects.get(store_ID=STORE_ID)
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
            "menuItems": meal_list
        }
        return Response(single_store)

    def post(self, request):
        sent_meal = json.loads(request.body)['meal']
        Meal.objects.filter(meal_hash=sent_meal["meal_hash"]).delete()
        store = Store.objects.get(store_ID=sent_meal["store_ID"])
        meal = Meal.objects.create(meal_hash=sent_meal["meal_hash"],
                                   title=sent_meal["title"],
                                   description=sent_meal["description"],
                                   price=sent_meal["price"],
                                   meal_owner=store)
        # if breaks remove meal_id
        meal.save()
        for question in sent_meal["questions"]:
            single_question = Question.objects.create(type=question["type"],
                                                      option_limit_lower=question["optionLimits"][0],
                                                      option_limit_upper=question["optionLimits"][1],
                                                      title=question["title"],
                                                      meal=meal)
            single_question.save()
            for option in question["options"]:
                single_option = Option.objects.create(option_text=option,
                                                      question=single_question)
                single_option.save()
        return Response("done")

# class singleMeal(APIView):
#
#     def post(self):
#         pass
