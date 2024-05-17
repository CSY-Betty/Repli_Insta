from django.urls import path

from . import api

app_name = "chat"

urlpatterns = [
    path("create-room/", api.create_room, name="create_room"),
    path("list-rooms/", api.list_rooms, name="list_rooms"),
    path("room/<str:room_id>/", api.room, name="room"),
]
