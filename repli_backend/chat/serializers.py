from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Conversation, ConversationMessage, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("uuid", "client", "agent")


class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = ("id", "users", "modified_at_formatted")


class ConversationMessageSeriazlizer(serializers.ModelSerializer):
    sent_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ("id", "sent_to", "created_by", "created_at_formatted", "body")


class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSeriazlizer(read_only=True, many=True)
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = ("id", "users", "modified_at_formatted", "messages")
