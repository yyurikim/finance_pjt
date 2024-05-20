from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Bulletin_comment, Bulletin_post, Challenge_comment, Challenge_post, Consumer_comment, Consumer_post
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser


# 자유게시판 view
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
def bulletin_index(request):
  if request.method == 'GET':
    posts = Bulletin_post.objects.all().order_by('-created_at')
    serializer = BulletinPostSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'POST':
    if request.user.is_authenticated:
      serializer = BulletinPostCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])
def bulletin_post_detail(request, post_pk):
  post = Bulletin_post.objects.get(pk=post_pk)
  if request.method == 'GET':
    serializer = BulletinPostSerializer(post, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'PUT':
    data = request.data.copy()
    data['user'] = request.user.pk  # 사용자 ID를 포함하여 요청 데이터 수정
    serializer = BulletinPostSerializer(post, data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['POST'])
def bulletin_comment_create(request):
  if request.user.is_authenticated:
    data = request.data.copy()
    data['post'] = request.data.get('post_id')
    serializer = BulletinCommentSerializer(data=data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def bulletin_comment_list(request, post_pk):
  comments = Bulletin_comment.objects.filter(post=post_pk)
  serializer = BulletinCommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def bulletin_comment_detail(request, comment_pk):
  comment = Bulletin_comment.objects.get(pk=comment_pk)
  if request.method == 'PUT':
    # comment = Bulletin_comment.objects.get(pk=request.data['comment_id'])
    serializer = BulletinCommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    # comment = Bulletin_comment.objects.get(pk=request.data['comment_id'])
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 소비게시판 view
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
def consumer_index(request):
  if request.method == 'GET':
    posts = Consumer_post.objects.all().order_by('-created_at')
    serializer = ConsumerPostSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'POST':
    if request.user.is_authenticated:
      serializer = ConsumerPostCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])
def consumer_post_detail(request, post_pk):
  post = Consumer_post.objects.get(pk=post_pk)
  if request.method == 'GET':
    serializer = ConsumerPostSerializer(post, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'PUT':
    data = request.data.copy()
    data['user'] = request.user.pk  # 사용자 ID를 포함하여 요청 데이터 수정
    serializer = ConsumerPostSerializer(post, data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET','POST'])
def consumer_buyit(request, post_pk):
  post = Consumer_post.objects.get(pk=post_pk)
  if request.method == 'GET':
    serializer = ConsumerVoteSerializer(post)
    return Response(serializer.data)
  else:
    user = request.user
    if request.user.is_authenticated:
      if user in post.buyit.all():
        post.buyit.remove(request.user)
      else:
        post.buyit.add(request.user)
        post.dontbuyit.remove(request.user)  # 다른 투표는 취소
      serializer = ConsumerVoteSerializer(post)
    print('POST')
    return Response(serializer.data)

@api_view(['POST'])
def consumer_dontbuyit(request, post_pk):
  post = Consumer_post.objects.get(pk=post_pk)
  user = request.user
  if request.user.is_authenticated:
    if user in post.dontbuyit.all():
      post.dontbuyit.remove(request.user)
    else:
      post.dontbuyit.add(request.user)
      post.buyit.remove(request.user)  # 다른 투표는 취소
    serializer = ConsumerVoteSerializer(post)
  return Response(serializer.data)


@api_view(['POST'])
def consumer_comment_create(request):
  if request.user.is_authenticated:
    data = request.data.copy()
    data['post'] = request.data.get('post_id')
    serializer = ConsumerCommentSerializer(data=data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def consumer_comment_list(request, post_pk):
  comments = Consumer_comment.objects.filter(post=post_pk)
  serializer = ConsumerCommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def consumer_comment_detail(request, comment_pk):
  comment = Consumer_comment.objects.get(pk=comment_pk)
  if request.method == 'PUT':
    # comment = Bulletin_comment.objects.get(pk=request.data['comment_id'])
    serializer = ConsumerCommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    # comment = Bulletin_comment.objects.get(pk=request.data['comment_id'])
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 소비게시판 view
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
def challenge_index(request):
  if request.method == 'GET':
    posts = Challenge_post.objects.all().order_by('-created_at')
    serializer = ChallengePostSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'POST':
    if request.user.is_authenticated:
      serializer = ChallengePostCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])
def challenge_post_detail(request, post_pk):
  post = Challenge_post.objects.get(pk=post_pk)
  if request.method == 'GET':
    serializer = ChallengePostSerializer(post, context={'request': request})
    return Response(serializer.data)
  elif request.method == 'PUT':
    data = request.data.copy()
    data['user'] = request.user.pk  # 사용자 ID를 포함하여 요청 데이터 수정
    serializer = ChallengePostSerializer(post, data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

@api_view(['POST'])
def challenge_comment_create(request):
  if request.user.is_authenticated:
    data = request.data.copy()
    data['post'] = request.data.get('post_id')
    serializer = ChallengeCommentSerializer(data=data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def challenge_comment_list(request, post_pk):
  comments = Challenge_comment.objects.filter(post=post_pk)
  serializer = ChallengeCommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def challenge_comment_detail(request, comment_pk):
  comment = Challenge_comment.objects.get(pk=comment_pk)
  if request.method == 'PUT':
    # comment = Bulletin_comment.objects.get(pk=request.data['comment_id'])
    serializer = ChallengeCommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    # comment = Bulletin_comment.objects.get(pk=request.data['comment_id'])
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
