from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from cabinet.models import Box, UserBox, Notification, UserNotification, Operation, Coin, UserBalance
from cabinet.serializers import (
    BoxSerializer,
    UserBoxListSerializer,
    NotificationSerializer,
    OperationSerializer,
    CoinSerializer,
    UserBalanceListSerializer,
    UserNotificationListSerializer,
    UserBalanceSerializer,
    UserBoxSerializer,
    UserNotificationSerializer,
)


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=["GET"],
        url_path="my-boxes",
        permission_classes=[permissions.IsAuthenticated],
    )
    def my_boxes(self, request):
        user_boxes = UserBox.objects.filter(user_id=request.user.id).select_related("box", "user")
        serializer = UserBoxListSerializer(user_boxes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=["GET"],
        url_path="my-notifications",
        permission_classes=[permissions.IsAuthenticated],
    )
    def my_notifications(self, request):
        user_notifications = UserNotification.objects.filter(user_id=request.user.id).select_related(
            "notification", "user"
        )
        serializer = UserNotificationListSerializer(user_notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.select_related("user", "box")
    serializer_class = OperationSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=["GET"],
        url_path="my-operations",
        permission_classes=[permissions.IsAuthenticated],
    )
    def my_operations(self, request):
        user_operations = Operation.objects.filter(user_id=request.user.id).select_related("user", "box")
        serializer = OperationSerializer(user_operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=["GET"],
        url_path="my-balance",
        permission_classes=[permissions.IsAuthenticated],
    )
    def my_balance(self, request):
        user_balance = UserBalance.objects.filter(user_id=request.user.id).select_related("user", "coin")
        serializer = UserBalanceListSerializer(user_balance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserBalanceViewSet(viewsets.ModelViewSet):
    queryset = UserBalance.objects.select_related("user", "coin")
    serializer_class = UserBalanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserBoxViewSet(viewsets.ModelViewSet):
    queryset = UserBox.objects.select_related("user", "box")
    serializer_class = UserBoxSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserNotificationViewSet(viewsets.ModelViewSet):
    queryset = UserNotification.objects.select_related("user", "notification")
    serializer_class = UserNotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
