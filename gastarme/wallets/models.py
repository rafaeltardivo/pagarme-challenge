from decimal import Decimal

from django.db import models

from users.models import User


class Wallet(models.Model):
    """Model for wallets."""
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='wallet'
    )
    credit_limit = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal('0.00')
    )
    credit_available = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'User: {} limit: {} available: {}'.format(
            self.user, self.credit_limit, self.credit_available
        )

    class Meta:
        ordering = ['id', ]


class CreditCard(models.Model):
    """Model for credit cards."""
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name='credit_cards'
    )
    number = models.CharField(max_length=16, unique=True)
    cardholder_name = models.CharField(max_length=26)
    cvv = models.CharField(max_length=3)
    expires_at = models.DateField()
    monthly_billing_day = models.PositiveIntegerField()
    limit = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal('0.00')
    )

    def __str__(self):
        return 'Wallet: {} number: {} limit: {} monthly_billing_day: {}'.format(
            self.wallet, self.number, self.limit, self.monthly_billing_day
        )

    class Meta:
        ordering = ['-monthly_billing_day', 'limit']
