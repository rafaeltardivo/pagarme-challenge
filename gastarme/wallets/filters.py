from django_filters import rest_framework as filters

from .models import Wallet, CreditCard


class WalletFilter(filters.FilterSet):
    """Filter for the wallet view."""

    class Meta:
        model = Wallet
        fields = ('user', 'id')


class CreditCardFilter(filters.FilterSet):
    """Filter for the wallet view."""

    class Meta:
        model = CreditCard
        fields = {
            'limit': ('lte', 'gte'),
            'expires_at': ('lte', 'gte')
        }
