from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
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