from django.urls import path
from apps.news.views import web as views

urlpatterns = [
    path('list', views.WebNewsListRetrieve.as_view()),
    path('categories', views.WebNewsCategoriesList.as_view())
]
