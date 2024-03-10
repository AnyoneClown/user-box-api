from rest_framework import generics, permissions

from cabinet.models import Box, UserBox
from cabinet.serializers import BoxSerializer, UserBoxListSerializer


class BoxDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyBoxesListView(generics.ListAPIView):
    serializer_class = UserBoxListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserBox.objects.filter(user_id=self.request.user.id).select_related("box", "user")


