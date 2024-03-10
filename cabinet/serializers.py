from rest_framework import serializers

from cabinet.models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"


class UserBoxListSerializer(serializers.ModelSerializer):
    box = BoxSerializer(many=False, read_only=True)

    class Meta:
        model = Box
        fields = ["box"]
