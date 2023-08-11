from django.shortcuts import render, get_object_or_404

from .models import Meal, Category
from contact.models import ContactDetail



def meals(request):

    contact_details = ContactDetail.objects.first()

    meals = Meal.objects.all()

    categories = Category.objects.prefetch_related('meal_set')

    context = {
        'meals':meals,
        'categories':categories,
        'contact_details':contact_details
    }

    return render(request, 'meals/list_of_meals.html', context)



def single_meal(request, meal_name):

    contact_details = ContactDetail.objects.first()

    single_meal = get_object_or_404(Meal,slug=meal_name)

    context = {
        'single_meal':single_meal,
        'contact_details':contact_details
    }

    return render(request, 'meals/single_meal.html', context)