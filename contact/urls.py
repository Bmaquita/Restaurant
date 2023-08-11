# reservation/urls.py
from django.urls import path

from . import views 


urlpatterns = [
    path('', views.contact, name='contact'), 
    path('reservation/', views.reservation, name = 'reservation'),
]
