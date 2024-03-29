from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed

from commons.permissions import IsRegularUser

from .filters import PurchaseFilter
from .models import Purchase
from .serializers import PurchaseSerializer

from . import logger


class PurchaseViewSet(ModelViewSet):
    """Viewset for purchases."""
    permission_classes = (IsRegularUser, )
    serializer_class = PurchaseSerializer
    filter_class = PurchaseFilter

    def get_queryset(self):
        user = self.request.user

        if user and hasattr(user, 'wallet'):
            queryset = Purchase.objects.filter(wallet=user.wallet)
        else:
            queryset = Purchase.objects.none()
        return queryset

    def create(self, request, *args, **kwargs):
        logger.info("Purchase create request", extra={'user': request.user})
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        logger.info("Purchase list request", extra={'user': request.user})
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info("Purchase detail request", extra={'user': request.user})
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
