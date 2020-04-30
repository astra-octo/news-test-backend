from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from apps.news.filters import NewsFilter
from apps.news.models import News, NewsCategory
from apps.news.serializers.web import WebNewsSerializer


class WebNewsListRetrieve(generics.RetrieveAPIView):
    queryset = News.objects.with_base_relations().active()
    serializer_class = WebNewsSerializer
    permission_classes = (AllowAny,)

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

    filterset_class = NewsFilter


class WebNewsCategoriesList(generics.RetrieveAPIView):
    queryset = NewsCategory.objects.active()

