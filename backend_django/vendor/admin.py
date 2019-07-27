from django.contrib import admin
from vendor.models import Store, Meal, Question, Option


# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_ID', 'name')
    ordering = ['store_ID']


class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_hash', 'title', 'description', 'price', 'meal_owner')
    ordering = ['meal_hash']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_hash', 'title', 'type', 'option_limit_lower', 'option_limit_upper', 'meal')
    ordering = ['question_hash']


class OptionAdmin(admin.ModelAdmin):
    list_display = ('option_hash', 'option_text', 'question')
    ordering = ['option_hash']


admin.site.register(Option, OptionAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Question, QuestionAdmin)
