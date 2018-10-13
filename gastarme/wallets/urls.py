from django.urls import path

from .views import WalletViewSet, CreditCardViewSet

urlpatterns = [
    path('', WalletViewSet, name='wallets'),
    path('cards/', CreditCardViewSet, name='creditcards'),
]
