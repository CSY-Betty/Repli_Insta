from django.http import JsonResponse

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from account.models import User, FriendshipRequest
from account.serializers import UserSerializer

from .forms import PostForm, AttachmentForm
from .models import Post, Like, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer

from django.contrib.auth.models import AnonymousUser


# Create your views here.


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def post_list(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


# 取得特定 profile 的 posts
@api_view(["GET"])
@permission_classes([])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    can_send_friendship_request = True

    # 驗證是否登入，有登入才需確認好友狀態
    if not isinstance(request.user, AnonymousUser):

        if request.user in user.friends.all():
            can_send_friendship_request = False

        check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
            created_by=user
        )
        check2 = FriendshipRequest.objects.filter(created_for=user).filter(
            created_by=request.user
        )

        if check1 or check2:
            can_send_friendship_request = False

    return JsonResponse(
        {
            "posts": posts_serializer.data,
            "user": user_serializer.data,
            "can_send_friendship_request": can_send_friendship_request,
        },
        safe=False,
    )


@api_view(["POST"])
def post_create(request):
    form = PostForm(request.POST)
    attachment = None
    attachment_form = AttachmentForm(request.POST, request.FILES)

    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        if attachment:
            post.attachments.add(attachment)

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({"error": "create post error."})


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    serializer = PostDetailSerializer(post)

    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def post_like(request, pk):
    post = Post.objects.get(pk=pk)

    if not (post.likes.filter(created_by=request.user)):
        like = Like.objects.create(created_by=request.user)

        post.likes_count = post.likes_count + 1
        post.likes.add(like)
        post.save()

        return JsonResponse({"message": "like created"})
    else:
        return JsonResponse({"message": "post already liked."})


@api_view(["POST"])
def post_create_comment(request, pk):
    comment = Comment.objects.create(
        body=request.data.get("body"), created_by=request.user
    )

    post = Post.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count = post.comments_count + 1
    post.save()

    serializer = CommentSerializer(comment)

    return JsonResponse(serializer.data, safe=False)


@api_view(["PUT"])
def post_edit(request, pk):

    post = Post.objects.filter(created_by=request.user).get(pk=pk)

    form = PostForm(request.data, instance=post)

    if request.FILES:
        attachment = None
        attachment_form = AttachmentForm(request.data, request.FILES)

        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.created_by = request.user
            attachment.save()

            if attachment:
                post.attachments.clear()
                post.attachments.add(attachment)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        form.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({"error": "Update post error."})


@api_view(["DELETE"])
def post_delete(request, pk):
    post = Post.objects.filter(created_by=request.user).get(pk=pk)
    post.delete()

    return JsonResponse({"message": "post deleted"})
