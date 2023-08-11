from django.urls import path 


from . import views 

urlpatterns =[
    path('', views.meals, name = 'meals_list'),
    path('<slug:meal_name>',views.single_meal, name = 'single_meal')
]