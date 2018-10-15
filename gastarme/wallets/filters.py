from django_filters import rest_framework as filters

from .models import Wallet


class WalletFilter(filters.FilterSet):
    """Filter for the wallet view."""

    class Meta:
        model = Wallet
        fields = ('user', 'id')
