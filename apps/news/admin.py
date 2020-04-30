from django.contrib import admin

from apps.news.models import News, NewsCategory


@admin.register(News)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsCategory)
class AuthorAdmin(admin.ModelAdmin):
    pass
