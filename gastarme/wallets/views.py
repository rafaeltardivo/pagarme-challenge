from django.db import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed, PermissionDenied

from commons.permissions import (
    IsUserCresteListOrSuperuserListDelete,
    IsRegularUser
)

from .models import Wallet, CreditCard
from .serializers import (
    WalletSerializer,
    CreditCardSerializer,
    SuperuserWalletSerializer
)
from .filters import WalletFilter, CreditCardFilter

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
            queryset = Wallet.objects.none()

            if user and hasattr(user, 'wallet'):
                pk = self.kwargs.get('pk')

                if pk:
                    if user.wallet.id == int(pk):
                        queryset = Wallet.objects.filter(pk=pk)
                    else:
                        raise PermissionDenied
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
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        logger.info("Wallet delete request", extra={'user': request.user})

        try:
            return super().destroy(request, *args, **kwargs)
        except models.ProtectedError:
            raise PermissionDenied("Can't delete due to related objects")


class CreditCardViewSet(ModelViewSet):
    """"CRUD view for creditcards."""
    permission_classes = (IsRegularUser, )
    serializer_class = CreditCardSerializer
    filter_class = CreditCardFilter

    def get_queryset(self):
        user = self.request.user
        queryset = CreditCard.objects.none()

        if user and hasattr(user, 'wallet'):
            wallet_pk = self.kwargs.get('wallet_pk')

            if wallet_pk:
                if user.wallet.id == int(wallet_pk):
                    queryset = CreditCard.objects.filter(wallet=wallet_pk)
                else:
                    raise PermissionDenied(
                        'You must only access your own wallet'
                    )
            else:
                queryset = CreditCard.objects.filter(wallet__user=user)

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
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        logger.info("CreditCard delete request", extra={'user': request.user})

        try:
            return super().destroy(request, *args, **kwargs)
        except models.ProtectedError:
            raise PermissionDenied("Can't delete due to related objects")
