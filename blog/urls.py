from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.all_news, name='all_news'),
    path('<slug:news_slug>/', views.single_news,name='single_news'),
    path('category/<slug:category>/', views.search_by_category, name='search'),
]