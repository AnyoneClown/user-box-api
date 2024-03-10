from django.urls import path
from rest_framework import routers

from cabinet.views import BoxViewSet, NotificationViewSet

router = routers.DefaultRouter()
router.register("boxes", BoxViewSet)
router.register("notifications", NotificationViewSet)

urlpatterns = [
] + router.urls

app_name = "cabinet"
