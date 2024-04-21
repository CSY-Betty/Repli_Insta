from django.http import JsonResponse

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer


# Create your views here.


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def post_list(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


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