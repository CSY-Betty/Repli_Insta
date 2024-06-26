from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm

from django.db.models import Q


from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .forms import SignupForm, ProfileForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer


@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "email": request.user.email,
            "avatar": request.user.get_avatar(),
        }
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
        message = form.errors.as_json()

    return JsonResponse({"message": message})


# 取得使用者的好友列表
@api_view(["GET"])
# @authentication_classes([])
# @permission_classes([])
def friends(request, pk):
    # 獲取特定的用戶資料
    user = User.objects.get(pk=pk)
    requests = []

    # 如果發送請求者是帳戶使用者，取得帳戶使用者收到的好友請求
    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.SENT
        )

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
def edit_profile(request):
    user = request.user
    email = request.data.get("email")

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({"message": "email already exists."})

    else:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()

        serializer = UserSerializer(user)

        return JsonResponse(
            {"message": "information updated.", "user": serializer.data}
        )


@api_view(["POST"])
def edit_password(request):
    user = request.user

    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()
        return JsonResponse({"message": "success"})
    else:
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


@api_view(["POST"])
def send_friendship_request(request, pk):
    user = User.objects.get(pk=pk)

    # 讀取接收者的清單與邀請者的清單是否已經存在相同的邀請
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )

    if not check1 or not check2:
        friendship_request = FriendshipRequest.objects.create(
            created_for=user, created_by=request.user
        )

        return JsonResponse({"friendship request": "friendship request created."})

    else:
        return JsonResponse({"friendship request": "request already sent."})


@api_view(["POST"])
def handle_request(request, pk, status):
    # 取得申請者的資料
    user = User.objects.get(pk=pk)

    # 讀取好友資料
    friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(
        created_by=user
    )

    if status == "acceptd":

        # 修改好友狀態
        friendship_request.status = status
        friendship_request.save()

        user.friends.add(request.user)
        user.friends_count = user.friends_count + 1
        user.save()

        request_user = request.user
        request_user.friends_count = request_user.friends_count + 1
        request_user.save()

    elif status == "rejected":

        friendship_request.delete()

    elif status == "removed":

        friendship_request.delete()

        friend_to_remove = User.objects.get(id=request.user.id)

        try:
            user.friends.remove(friend_to_remove)
            user.friends_count = user.friends_count - 1
            user.save()
        except Exception as e:
            print("Error occurred while removing friend:", e)

        request_user = request.user
        request_user.friends.remove(user)
        request_user.friends_count = request_user.friends_count - 1
        request_user.save()

    return JsonResponse({"message": "friendship request updated"})
