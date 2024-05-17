from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Message, Room


class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("id", "body", "created_at", "created_by")


class RoomSerializer(serializers.ModelSerializer):
    participants1 = UserSerializer(read_only=True)
    participants2 = UserSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ("id", "participants1", "participants2")
