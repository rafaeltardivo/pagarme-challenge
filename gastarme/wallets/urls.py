from rest_framework.routers import DefaultRouter

from .views import WalletViewSet, CreditCardViewSet

router = DefaultRouter()
router.register('creditcards', CreditCardViewSet, 'creditcards')
router.register('', WalletViewSet, 'wallets')
urlpatterns = router.urls
