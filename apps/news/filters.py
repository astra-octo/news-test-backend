from django_filters import rest_framework as filters
from django_filters.constants import EMPTY_VALUES

from apps.news.models import News, NewsQuerySet


class NewsFilter(filters.FilterSet):
    category = filters.CharFilter(method='by_category')

    class Meta:
        model = News
        fields = ['category']

    @staticmethod
    def by_category(queryset: NewsQuerySet, _, value: str):
        if value not in EMPTY_VALUES:
            return queryset.for_categories(value.split('__'))
        return queryset
