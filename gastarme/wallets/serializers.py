from rest_framework import serializers

from .models import Wallet, CreditCard


class WalletSerializer(serializers.ModelSerializer):
    """Serializer for the model Wallet."""

    class Meta:
        model = Wallet
        fields = ('__all__')


class CreditCardSerializer(serializers.ModelSerializer):
    """Serializer for the model CreditCard."""

    class Meta:
        model = CreditCard
        fields = ('__all__')
