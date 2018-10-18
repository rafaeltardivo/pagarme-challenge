from decimal import Decimal

import factory

from purchases.models import Purchase
from wallets.tests.factories import WalletFactory


class PurchaseFactory(factory.django.DjangoModelFactory):
    """Factory for the model Wallet."""

    class Meta:
        model = Purchase

    wallet = factory.SubFactory(WalletFactory)
    value = Decimal('100.00')
