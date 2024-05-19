from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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