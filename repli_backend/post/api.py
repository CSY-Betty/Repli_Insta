from django.http import JsonResponse

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from account.models import User
from account.serializers import UserSerializer

from .forms import PostForm
from .models import Post, Like, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer


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
@authentication_classes([])
@permission_classes([])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse(
        {"posts": posts_serializer.data, "user": user_serializer.data}, safe=False
    )


@api_view(["POST"])
def post_create(request):
    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

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
