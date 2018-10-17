from django_filters import rest_framework as filters

from .models import Wallet, CreditCard


class WalletFilter(filters.FilterSet):
    """Filter for the wallet view."""

    class Meta:
        model = Wallet
        fields = ('user', 'id')


class CreditCardFilter(filters.FilterSet):
    """Filter for the wallet view."""
    limit_min = filters.NumberFilter(field_name='limit', lookup_expr='gte')
    limit_max = filters.NumberFilter(field_name='limit', lookup_expr='lte')
    expires_at_min = filters.DateFilter(
        field_name='expires_at',
        lookup_expr='gte'
    )
    expires_at_max = filters.DateFilter(
        field_name='expires_at',
        lookup_expr='lte'
    )

    class Meta:
        model = CreditCard
        fields = ('limit_min', 'limit_max', 'expires_at_min', 'expires_at_max')
