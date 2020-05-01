from rest_framework import pagination
from rest_framework.response import Response


class BasePaginator(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'prev': self.page.previous_page_number() if self.page.has_previous() else None,
            'current': self.page.number,
            'data': data,
        })
