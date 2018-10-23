from decimal import Decimal

from django.db import models

from wallets.models import CreditCard


class Bill(models.Model):
    """Model for bills."""

    credit_card = models.ForeignKey(
        CreditCard,
        on_delete=models.PROTECT,
        related_name='purchases'
    )
    expires_at = models.DateField()
    value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal('0.00')
    )

    def __str__(self):
        return 'Credit card: {} expires_at: {} value: {}'.format(
            self.credit_card.id, self.expires_at, self.value
        )

    class Meta:
        ordering = ['id', ]
        unique_together = ('credit_card', 'expires_at')
