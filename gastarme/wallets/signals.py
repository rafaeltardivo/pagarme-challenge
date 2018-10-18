from decimal import Decimal

from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save

from .models import CreditCard
from purchases.models import Purchase


@receiver(post_save, sender=CreditCard)
def update_wallet_credit_limit(sender, instance, created, **kwargs):
    """Receiver for the Creditcard post-save signal that will update
       the CreditCard itself and it's related Wallet.
    """

    if created:
        # sets the limit to available
        instance.available = instance.limit
        instance.save()

        # updates related wallet limit and available
        related_wallet = instance.wallet
        related_wallet.credit_limit += Decimal(instance.limit)
        related_wallet.credit_available += Decimal(instance.limit)
        related_wallet.save()


@receiver(post_save, sender=Purchase)
def payment(sender, instance, **kwargs):
    """Receiver for the Creditcard post-save signal that will update
       credit limits.
    """
    purchase_value = instance.value
    wallet = instance.wallet
    cards = wallet.credit_cards.all()

    for card in cards:

        if not purchase_value:
            break

        if purchase_value > card.available:
            card.available = 0
            purchase_value -= card.available
        else:
            card.available -= purchase_value
            purchase_value = 0
        card.save()

    result = CreditCard.objects.aggregate(Sum('available'))
    wallet.credit_available = result['available__sum']
    wallet.save()
