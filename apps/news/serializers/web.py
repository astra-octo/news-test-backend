import time

from rest_framework import serializers

from apps.news.models import News
from apps.news.serializers.common import BaseNewsSerializer, BaseNewsCategorySerializer


class WebNewsSerializer(BaseNewsSerializer):
    created_timestamp = serializers.SerializerMethodField(read_only=True)

    class Meta(BaseNewsSerializer.Meta):
        fields = BaseNewsSerializer.Meta.fields + ['created_timestamp']

    @staticmethod
    def get_created_timestamp(obj: News) -> int:
        return int(time.mktime(obj.created_at.timetuple())*1000)


class WebNewsCategorySerializer(BaseNewsCategorySerializer):
    pass
