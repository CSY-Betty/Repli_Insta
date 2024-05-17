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


# class ConversationSerializer(serializers.ModelSerializer):
#     users = UserSerializer(read_only=True, many=True)

#     class Meta:
#         model = Conversation
#         fields = ("id", "users", "modified_at_formatted")


# class ConversationMessageSeriazlizer(serializers.ModelSerializer):
#     sent_to = UserSerializer(read_only=True)
#     created_by = UserSerializer(read_only=True)

#     class Meta:
#         model = ConversationMessage
#         fields = ("id", "sent_to", "created_by", "created_at_formatted", "body")


# class ConversationDetailSerializer(serializers.ModelSerializer):
#     messages = ConversationMessageSeriazlizer(read_only=True, many=True)
#     users = UserSerializer(read_only=True, many=True)

#     class Meta:
#         model = Conversation
#         fields = ("id", "users", "modified_at_formatted", "messages")
