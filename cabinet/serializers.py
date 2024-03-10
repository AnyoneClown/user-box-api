from rest_framework import serializers

from cabinet.models import Box, Notification, UserNotification


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"


class UserBoxListSerializer(serializers.ModelSerializer):
    box = BoxSerializer(many=False, read_only=True)

    class Meta:
        model = Box
        fields = ["box"]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class UserNotificationSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer(many=False, read_only=True)

    class Meta:
        model = UserNotification
        fields = ["notification", "date"]
