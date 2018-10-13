from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Wallet, CreditCard
from .serializers import WalletSerializer, CreditCardSerializer

from . import logger


class WalletViewSet(ModelViewSet):
    """CRUD view for wallets."""
    permission_classes = (IsAuthenticated, )
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def create(self, request, *args, **kwargs):
        logger.info("Wallet create request", extra={'user': request.user})
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        logger.info("Wallet list request", extra={'user': request.user})
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info("Wallet update request", extra={'user': request.user})
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.info("Wallet delete request", extra={'user': request.user})
        return super().destroy(request, *args, **kwargs)


class CreditCardViewSet(ModelViewSet):
    """"CRUD view for creditcards."""
    permission_classes = (IsAuthenticated, )
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

    def create(self, request, *args, **kwargs):
        logger.info("CreditCard create request", extra={'user': request.user})
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        logger.info("CreditCard list request", extra={'user': request.user})
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info("CreditCard update request", extra={'user': request.user})
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.info("CreditCard delete request", extra={'user': request.user})
        return super().destroy(request, *args, **kwargs)
