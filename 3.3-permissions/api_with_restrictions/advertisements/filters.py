from django_filters import rest_framework as filters, DateFromToRangeFilter, NumberFilter
from rest_framework.filters import SearchFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()


    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
