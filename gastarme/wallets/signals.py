from decimal import Decimal

from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save

from purchases.models import Purchase
from .models import CreditCard
from .services import set_payment_records


@receiver(post_save, sender=CreditCard)
def update_wallet_post_create_card(sender, instance, created, **kwargs):
    """Receiver for the Creditcard post-save signal that will update
       the CreditCard itself and it's related Wallet.
    """

    if created:
        # sets the available limit
        instance.available = instance.limit
        instance.save()

        # updates related wallet limit and available
        related_wallet = instance.wallet

        related_wallet.credit_available = Decimal('0.00')
        related_wallet.credit_limit += Decimal(instance.limit)
        related_wallet.credit_available += Decimal(instance.limit)
        related_wallet.save()


@receiver(post_save, sender=Purchase)
def update_wallet_post_purchase(sender, instance, **kwargs):
    """Receiver for the Purchase post-save signal that will update
       credit limits.
    """
    wallet = instance.wallet
    cards = wallet.credit_cards.all()

    set_payment_records(cards, instance)

    result = CreditCard.objects.aggregate(Sum('available'))
    wallet.credit_available = result['available__sum']
    wallet.save()
