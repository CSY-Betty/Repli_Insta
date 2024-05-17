import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer

from django.utils.timesince import timesince


from account.models import User
from .models import Room, Message

from account.serializers import UserSerializer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.get_room()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        # Receive message from WebSocket (front end)
        text_data_json = json.loads(text_data)
        type = text_data_json["type"]
        message = text_data_json["message"]
        name = text_data_json["name"]

        if type == "message":
            new_message = await self.create_message(message, name)
            name = await self.get_created_data(name)

            # Send message to group / room
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "name": name,
                    "created_at": timesince(new_message.created_at),
                },
            )

    async def chat_message(self, event):
        # Send message to WebSocket (front end)
        await self.send(
            text_data=json.dumps(
                {
                    "type": event["type"],
                    "message": event["message"],
                    "name": event["name"],
                }
            )
        )

    @sync_to_async
    def get_room(self):
        self.room = Room.objects.get(id=self.room_name)

    @sync_to_async
    def create_message(self, message, created_by):
        message = Message.objects.create(body=message)

        message.created_by = User.objects.get(pk=created_by)
        message.save()

        self.room.messages.add(message)

        return message

    @sync_to_async
    def get_created_data(self, name):
        name = User.objects.get(pk=name)
        print("get_created_data: ", name)
        name = UserSerializer(name).data

        return name
