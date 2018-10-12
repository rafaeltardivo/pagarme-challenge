from django.db import models

from users.models import User


class Wallet(models.Model):
    """Model for wallets."""
    user = models.OneToOneField(
        User,
        on_deleteon_delete=models.PROTECT,
        related_name='wallet'
    )
    credit_limit = models.DecimalField(max_digits=8, decimal_places=2)
    credit_available = models.DecimalField(max_digits=8, decimal_places=2)


class CreditCard(models.Model):
    """Model for credit cards."""
    wallet = models.ForeignKey(
        Wallet,
        on_deleteon_delete=models.PROTECT,
        related_name='credit_cards'
    )
    number = models.CharField(max_length=16)
    cardholder_name = models.charfield(max_length=26)
    cvv = models.CharField(max_length=3)
    expires_at = models.DateField()
    billing_date = models.DateField()
    limit = models.DecimalField(max_digits=8, decimal_places=2)
