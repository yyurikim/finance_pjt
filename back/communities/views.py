from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
  if request.method == 'GET':
    posts = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    if request.user.is_authenticated:
      serializer = PostCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

def post_detail(request):
  pass

def comment_detail(request):
  pass
