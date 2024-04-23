from django.http import JsonResponse

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .forms import SignupForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer


@api_view(["GET"])
def me(request):
    return JsonResponse(
        {"id": request.user.id, "name": request.user.name, "email": request.user.email}
    )


# Set the 'authentication_classes' and 'permission_classes' decorators to be empty so that we can access this view without being authenticated.
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data

    message = "success"

    form = SignupForm(
        {
            "email": data.get("email"),
            "name": data.get("name"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    if form.is_valid():
        form.save()
    else:
        message = "error"
        # message = form.errors.as_json()

    return JsonResponse({"message": message})


# 取得使用者的好友列表
@api_view(["GET"])
def friends(request, pk):
    # 獲取特定的用戶資料
    user = User.objects.get(pk=pk)
    requests = []

    # 如果發送請求者是帳戶使用者，取得帳戶使用者收到的好友請求
    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user)

    # 獲取特定用戶的好友資料
    friends = user.friends.all()

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": FriendshipRequestSerializer(requests, many=True).data,
        },
        safe=False,
    )


@api_view(["POST"])
def send_friendship_request(request, pk):
    user = User.objects.get(pk=pk)

    friendship_request = FriendshipRequest(created_for=user, created_by=request.user)

    return JsonResponse({"friendship request": "friendship request created"})
