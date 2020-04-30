from django.urls import path
from apps.news.views import web as views

urlpatterns = [
    path('list', views.WebNewsList.as_view(), name='web-news-list'),
    path('categories', views.WebNewsCategoriesList.as_view(), name='web-news-categories-list')
]
