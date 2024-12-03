from django.shortcuts import render
from .models import Meal


def meal_list(request):

    return render(request, "meals/list.html")