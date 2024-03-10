from django.urls import path
from rest_framework import routers

from cabinet.views import BoxViewSet

router = routers.DefaultRouter()
router.register("boxes", BoxViewSet)


urlpatterns = [
] + router.urls

app_name = "cabinet"
