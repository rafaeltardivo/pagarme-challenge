from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import BillViewSet

router = routers.SimpleRouter()
router.register('', BillViewSet, base_name='billings')

urlpatterns = [
    url('', include(router.urls)),
]
