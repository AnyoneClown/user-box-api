from django.urls import path
from rest_framework import routers

from cabinet.views import BoxViewSet, NotificationViewSet, OperationViewSet, CoinViewSet, UserNotificationViewSet, UserBalanceViewSet, UserBoxViewSet

router = routers.DefaultRouter()
router.register("boxes", BoxViewSet)
router.register("notifications", NotificationViewSet)
router.register("operations", OperationViewSet)
router.register("coins", CoinViewSet)

router.register("user-boxes", UserBoxViewSet)
router.register("user-notifications", UserNotificationViewSet)
router.register("user-balances", UserBalanceViewSet)


urlpatterns = router.urls

app_name = "cabinet"
