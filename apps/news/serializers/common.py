from rest_framework import serializers

from apps.news.models import News, NewsCategory


class BaseNewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = [
            'id',
            'name',
        ]


class BaseNewsSerializer(serializers.ModelSerializer):
    categories = BaseNewsCategorySerializer(many=True)

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'categories',
            'created_at',
        ]
