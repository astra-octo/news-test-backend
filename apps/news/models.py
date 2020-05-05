from django.db import models
from django.utils import timezone

from apps.main.models import BaseModel


class NewsCategoryQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    objects = NewsCategoryQuerySet.as_manager()

    def __str__(self):
        return self.name


class NewsQuerySet(models.QuerySet):
    def with_base_relations(self):
        return self.prefetch_related('categories')

    def annotate_has_active_category(self):
        return self.annotate(has_active_category=models.Case(
            models.When(
                categories__is_active=True, then=True
            ),
            default=False,
            output_field=models.BooleanField(),
        ))

    def active(self):
        return self.annotate_has_active_category().filter(
            published_at__lte=timezone.now(),
            has_active_category=True,
        )

    def for_categories(self, categories: list):
        return self.filter(
            categories__in=categories
        )


class News(BaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField()

    categories = models.ManyToManyField(
        NewsCategory,
        related_name='news',
    )

    is_publish = models.BooleanField(default=False)

    published_at = models.DateField(auto_now_add=True)

    objects = NewsQuerySet.as_manager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
