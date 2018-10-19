from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed

from commons.permissions import IsRegularUser

from .models import Purchase
from .serializers import PurchaseSerializer

from . import logger


class PurchaseViewSet(ModelViewSet):
    """Create view for purchases."""
    permission_classes = (IsRegularUser, )
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

    def post(self, request, *args, **kwargs):
        logger.info("Purchase create request", extra={'user': request.user})
        return super().post(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        logger.info("Purchase list request", extra={'user': request.user})
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info("Wallet detail request", extra={'user': request.user})
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
