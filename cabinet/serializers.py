from rest_framework import serializers

from cabinet.models import Box, Notification, UserNotification, Operation, Coin, UserBalance, UserBox


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"


class UserBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBox
        fields = "__all__"


class UserBoxListSerializer(serializers.ModelSerializer):
    box = BoxSerializer(many=False, read_only=True)

    class Meta:
        model = UserBox
        fields = ["box", "status"]


class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class UserNotificationListSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer(many=False, read_only=True)

    class Meta:
        model = UserNotification
        fields = ["notification", "date"]


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = "__all__"


class UserBalanceListSerializer(serializers.ModelSerializer):
    coin = CoinSerializer(many=False, read_only=True)

    class Meta:
        model = UserBalance
        fields = ["coin", "balance"]
