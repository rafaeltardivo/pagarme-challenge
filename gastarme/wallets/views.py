from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from commons.permissions import IsUserCresteListOrSuperuserListDelete
from .models import Wallet, CreditCard
from .serializers import (
    WalletSerializer,
    CreditCardSerializer,
    SuperuserWalletSerializer
)
from .filters import WalletFilter

from . import logger


class WalletViewSet(ModelViewSet):
    """CRUD view for wallets."""
    permission_classes = (IsUserCresteListOrSuperuserListDelete, )
    filter_class = WalletFilter

    def get_queryset(self):
        user = self.request.user

        if user and user.is_superuser:
            queryset = Wallet.objects.all()
        else:
            queryset = Wallet.objects.filter(user=user)
        return queryset

    def get_serializer_class(self):
        user = self.request.user

        if user and user.is_superuser:
            serializer = SuperuserWalletSerializer
        else:
            serializer = WalletSerializer
        return serializer

    def create(self, request, *args, **kwargs):
        logger.info("Wallet create request", extra={'user': request.user})

        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        logger.info("Wallet list request", extra={'user': request.user})

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info("Wallet list request", extra={'user': request.user})

        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info("Wallet update request", extra={'user': request.user})

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.info("Wallet delete request", extra={'user': request.user})

        return super().destroy(request, *args, **kwargs)


class CreditCardViewSet(ModelViewSet):
    """"CRUD view for creditcards."""
    permission_classes = (IsAuthenticated, )
    serializer_class = CreditCardSerializer

    def get_queryset(self):
        user = self.request.user

        if user and hasattr(user, 'wallet'):
            queryset = user.wallet.credit_cards.all()
        else:
            queryset = CreditCard.objects.none()
        return queryset

    def create(self, request, *args, **kwargs):
        logger.info("CreditCard create request", extra={'user': request.user})

        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        logger.info("CreditCard list request", extra={'user': request.user})

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info("CreditCard detail request", extra={'user': request.user})

        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info("CreditCard update request", extra={'user': request.user})

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.info("CreditCard delete request", extra={'user': request.user})

        return super().destroy(request, *args, **kwargs)
