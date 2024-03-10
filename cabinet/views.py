from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from cabinet.models import Box, UserBox, Notification, UserNotification, Operation
from cabinet.serializers import BoxSerializer, UserBoxListSerializer, NotificationSerializer, \
    UserNotificationSerializer, OperationSerializer


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
        user_notifications = UserNotification.objects.filter(user_id=request.user.id).select_related("notification", "user")
        serializer = UserNotificationSerializer(user_notifications, many=True)
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
