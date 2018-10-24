from decimal import Decimal

from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


from commons.permissions import IsRegularUser

from .models import Bill
from .serializers import BillSerializer, BillPaySerializer
from .services import pay_bill
from .filters import BillFilter
from . import logger


class BillViewSet(ReadOnlyModelViewSet):
    """Read only viewset for bills."""
    permission_classes = (IsRegularUser, )
    serializer_class = BillSerializer
    filter_class = BillFilter

    def get_queryset(self):
        user = self.request.user

        if user and hasattr(user, 'wallet'):
            queryset = Bill.objects.filter(
                credit_card__wallet=user.wallet,
                value__gt=0
            )
        else:
            queryset = Bill.objects.none()
        return queryset

    def list(self, request, *args, **kwargs):
        logger.info("Bill list request", extra={'user': request.user})
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info("Bill detail request", extra={'user': request.user})
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['patch'], permission_classes=[IsRegularUser])
    def pay(self, request, pk=None):
        """Action route for paying bills."""
        logger.info("Bill pay request", extra={'user': request.user})
        bill = self.get_object()
        serializer = BillPaySerializer(data=request.data)

        if serializer.is_valid():
            value_paid = Decimal(serializer.data['value'])

            if value_paid > bill.value:
                return Response(
                    'Value is greater than the current total',
                    status=status.HTTP_400_BAD_REQUEST
                )

            pay_bill(bill, value_paid)
            return Response(BillSerializer(instance=bill).data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
