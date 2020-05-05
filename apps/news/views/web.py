from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from apps.news.filters import NewsFilter
from apps.news.models import News, NewsCategory
from apps.news.serializers.web import WebNewsSerializer, WebNewsCategorySerializer
from apps.main.paginators import BasePaginator


class WebNewsList(generics.ListAPIView):
    queryset = News.objects.with_base_relations().active()
    serializer_class = WebNewsSerializer
    permission_classes = (AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsFilter

    pagination_class = BasePaginator


class WebNewsCategoriesList(generics.ListAPIView):
    queryset = NewsCategory.objects.active()
    serializer_class = WebNewsCategorySerializer

    pagination_class = None


