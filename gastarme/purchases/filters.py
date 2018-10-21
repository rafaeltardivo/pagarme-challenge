from django_filters import rest_framework as filters

from .models import Purchase


class PurchaseFilter(filters.FilterSet):
    """Filter for the purchase view."""

    class Meta:
        model = Purchase
        fields = {
            'made_at': ('lte', 'gte')
        }
