from rest_framework.routers import DefaultRouter

from .views import WalletViewSet, CreditCardViewSet

router = DefaultRouter()
router.register('', WalletViewSet, 'wallets')
router.register('creditcards', CreditCardViewSet, 'creditcards')
urlpatterns = router.urls
