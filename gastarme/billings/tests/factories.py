from datetime import date
from decimal import Decimal
import factory

from wallets.tests.factories import CreditCardFactory
from billings.models import Bill


class BillFactory(factory.django.DjangoModelFactory):
    """Factory for the bill model."""

    class Meta:
        model = Bill

    credit_card = factory.SubFactory(CreditCardFactory)
    value = Decimal('100.00')
    expires_at = date(2018, 12, 31)
