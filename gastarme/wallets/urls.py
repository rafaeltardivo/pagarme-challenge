from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import WalletViewSet, CreditCardViewSet

router = routers.SimpleRouter()
router.register('', WalletViewSet, base_name='wallets')

wallets_router = routers.NestedSimpleRouter(router, '', lookup='wallet')
wallets_router.register(
    'creditcards',
    CreditCardViewSet,
    base_name='wallet-creditcards'
)

urlpatterns = [
    url('', include(router.urls)),
    url('', include(wallets_router.urls)),
]
