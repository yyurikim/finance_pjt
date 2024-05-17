from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer
from rest_framework.parsers import MultiPartParser, FormParser



# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
def index(request):
  if request.method == 'GET':
    posts = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'POST':
    if request.user.is_authenticated:
      serializer = PostCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  if request.method == 'GET':
    serializer = PostSerializer(post, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'PUT':
    data = request.data.copy()
    data['user'] = request.user.pk  # 사용자 ID를 포함하여 요청 데이터 수정
    serializer = PostSerializer(post, data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

def comment_detail(request):
  pass
