from rest_framework.generics import CreateAPIView

from commons.permissions import IsRegularUser

from .models import Purchase
from .serializers import PurchaseSerializer

from . import logger


class PurchaseCreateView(CreateAPIView):
    """Create view for purchases."""
    permission_classes = (IsRegularUser, )
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

    def post(self, request, *args, **kwargs):
        logger.info("Purchase create request", extra={'user': request.user})
        return super().post(request, *args, **kwargs)
