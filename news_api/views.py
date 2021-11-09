from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from news_api.models import Post, Comment, Upvote
from news_api.serializers import PostSerializer, PostDetailSerializer, CommentSerializer


@api_view(["GET", "POST"])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def posts_list(request, format=None):
    """
    List all posts, or create a new post.
    """
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def post_detail(request, pk, format=None):
    """
    Retrieve, update or delete a post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PostDetailSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes((permissions.IsAuthenticated,))
def post_upvote(request, pk, format=None):
    """
    Upvote post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        user_upvote = post.upvotes.filter(author_id=request.user.id)
        if user_upvote:
            user_upvote.delete()
        else:
            user_upvote = Upvote(author=request.user, post=post)
            user_upvote.save()

        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(["POST"])
@permission_classes((permissions.IsAuthenticated,))
def create_comment(request, pk):
    """
    Create comment of post
    """
    try:
        Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = Comment(**serializer.data)
            comment.author = request.user
            comment.post_id = pk
            comment.save()
            return Response(comment)
