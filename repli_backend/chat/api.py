import json

from django.http import JsonResponse

from rest_framework.decorators import api_view

from django.db.models import Q


from .models import Room
from account.models import User

from .serializers import RoomSerializer, MessageSerializer


@api_view(["POST"])
def create_room(request):

    participants1 = request.user

    participants2 = request.POST.get("chatId", "")
    participants2 = User.objects.get(id=participants2)

    check = Room.objects.filter(
        Q(participants1=participants1, participants2=participants2)
        | Q(participants1=participants2, participants2=participants1)
    )

    if check.exists():
        room_id = check.first().id
    else:
        chat_room = Room.objects.create(
            participants1=participants1, participants2=participants2
        )

        room_id = chat_room.id

    return JsonResponse({"room_id": room_id})


@api_view(["GET"])
def list_rooms(request):
    rooms = Room.objects.filter(
        Q(participants1=request.user) | Q(participants2=request.user)
    )
    print(rooms)

    serializers = RoomSerializer(rooms, many=True)

    return JsonResponse({"rooms": serializers.data})


@api_view(["GET"])
def room(request, room_id):
    room = Room.objects.get(id=room_id)
    room_serializer = RoomSerializer(room)

    messages = room.messages.all()
    message_data = MessageSerializer(messages, many=True)

    return JsonResponse({"room": room_serializer.data, "messages": message_data.data})
