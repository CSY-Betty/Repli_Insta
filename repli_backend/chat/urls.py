from django.urls import path

from . import api

app_name = "chat"

urlpatterns = [
    path("", api.conversation_list, name="conversation_list"),
    path("<uuid:pk>/", api.conversation_detail, name="conversation_detail"),
    path(
        "<uuid:pk>/send/",
        api.conversation_send_message,
        name="conversation_send_message",
    ),
    path(
        "<uuid:user_pk>/get-or-create/",
        api.conversation_get_or_create,
        name="conversation_get_or_create",
    ),
    # asgi test
    path("create-room/<str:uuid>/", api.create_room, name="create_room"),
    path("get-room/", api.get_room, name="get-room"),
]
