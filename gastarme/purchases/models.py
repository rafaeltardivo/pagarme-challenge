from django.db import models

from wallets.models import Wallet, CreditCard


class Purchase(models.Model):
    """Model for purchases."""

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name='purchases'
    )
    value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    made_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Wallet: {} value: {} made_at: {}'.format(
            self.wallet, self.value, self.made_at
        )


class Payment(models.Model):
    """Model for the wallet's bill."""

    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.PROTECT,
        related_name='payments'
    )

    credit_card = models.ForeignKey(
        CreditCard,
        on_delete=models.PROTECT,
        related_name='credit_card_records'
    )

    value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
