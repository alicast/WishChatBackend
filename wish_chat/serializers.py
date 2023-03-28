from rest_framework import serializers

from . import models


class GroupUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GroupUsers
        fields = [
            "last_updated",
            "created",
            "user",
            "group",
        ]

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = [
            "created",
            "group_name",
            "last_updated",
        ]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "created",
            "last_updated",
            "django_user",
        ]

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = [
            "created",
            "last_updated",
            "Anonymous",
            "Text",
            "group",
            "user",
        ]
