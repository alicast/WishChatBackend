from rest_framework import viewsets, permissions

from . import serializers
from . import models


class GroupUsersViewSet(viewsets.ModelViewSet):
    """ViewSet for the GroupUsers class"""

    queryset = models.GroupUsers.objects.all()
    serializer_class = serializers.GroupUsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the Group class"""

    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the User class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Message class"""

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
