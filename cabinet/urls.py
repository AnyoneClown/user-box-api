from django.urls import path
from rest_framework import routers

from cabinet.views import BoxViewSet, NotificationViewSet, OperationViewSet, CoinViewSet

router = routers.DefaultRouter()
router.register("boxes", BoxViewSet)
router.register("notifications", NotificationViewSet)
router.register("operations", OperationViewSet)
router.register("coins", CoinViewSet)

urlpatterns = [] + router.urls

app_name = "cabinet"
