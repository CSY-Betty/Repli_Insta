from django.http import JsonResponse

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from account.models import User

from .models import Conversation, ConversationMessage, Room

from .serializers import (
    ConversationSerializer,
    ConversationDetailSerializer,
    ConversationMessageSeriazlizer,
    RoomSerializer,
)


@api_view(["GET"])
def conversation_list(request):
    conversations = Conversation.objects.filter(users__in=list([request.user]))

    serializer = ConversationSerializer(conversations, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def conversation_detail(request, pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(
        pk=pk
    )

    serializer = ConversationDetailSerializer(conversation)

    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def conversation_get_or_create(request, user_pk):
    user = User.objects.get(pk=user_pk)

    conversations = Conversation.objects.filter(users__in=list([request.user])).filter(
        users__in=list([user])
    )

    if conversations.exists():
        conversation = conversations.first()

    else:
        conversation = Conversation.objects.create()
        conversation.users.add(user, request.user)
        conversation.save()

    serializer = ConversationDetailSerializer(conversation)

    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def conversation_send_message(request, pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(
        pk=pk
    )

    for user in conversation.users.all():
        if user != request.user:
            sent_to = user

    conversation_message = ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data.get("body"),
        created_by=request.user,
        sent_to=sent_to,
    )

    serializer = ConversationMessageSeriazlizer(conversation_message)

    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def create_room(request, uuid):
    name = request.POST.get("name", "")
    url = request.POST.get("url", "")

    print(name)
    print(url)

    # Room.objects.create(uuid=uuid, client=name, url=url)

    return JsonResponse({"message": "room created"})


@api_view(["Get"])
def get_room(request):
    chat_room = Room.objects.filter(client__in=list([request.user]))
    print("request: ", request)
    print("request.user: ", request.user)

    print(chat_room)

    serializer = RoomSerializer(chat_room, many=True)

    return JsonResponse(serializer.data, safe=False)

    # return JsonResponse({"message": "room created"})


def chatPage():
    pass
