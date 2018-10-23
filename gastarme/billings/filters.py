from django_filters import rest_framework as filters

from .models import Bill


class BillFilter(filters.FilterSet):
    """Filter for the billings view."""

    class Meta:
        model = Bill
        fields = {
            'expires_at': ('lte', 'gte')
        }
