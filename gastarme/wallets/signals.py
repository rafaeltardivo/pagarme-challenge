from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import CreditCard


@receiver(pre_save, sender=CreditCard)
def update_credit_available(sender, instance, **kwargs):
    """Receiver for the Creditcard pre-save signal that will update
       non-set available limits.
    """

    if not instance.limit:
        instance.available = instance.limit


@receiver(post_save, sender=CreditCard)
def update_wallet_credit_limit(sender, instance, **kwargs):
    """Receiver for the Creditcard post-save signal that will update
       the CreditCard itself and it's related Wallet.
    """
    related_wallet = instance.wallet

    if not related_wallet.credit_limit:
        related_wallet.credit_limit += instance.limit
    if not related_wallet.credit_available:
        related_wallet.credit_available += instance.limit
    related_wallet.save()
