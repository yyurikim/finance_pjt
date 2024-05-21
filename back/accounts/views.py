from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404


# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# class CreateUserView(generics.CreateAPIView):
#     serializer_class = UserSerializer

User = get_user_model()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response(status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_type(request):
    user_type = request.data.get('user_type')
    
    user = request.user
    serializer = UserTypeSerializer(user, data={'user_type': user_type})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_goal(request):
    saving_amount = request.data.get('saving_amount')
    deposit_amount = request.data.get('deposit_amount')
    user_goal = request.data.get('my_goal')
    
    user = request.user
    serializer = UserGoalSerializer(user, data={'saving_amount': saving_amount, 'deposit_amount': deposit_amount, 'my_goal': user_goal})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    user = request.user
    serializer = UserUpdateSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
