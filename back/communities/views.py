from django.shortcuts import render
from rest_framework import api_view
from rest_framework import status

from django.contrib.auth import get_user_model
from .models import Post, Comment
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post, Comment

# Create your views here.

@api_view(['GET', 'POST'])
def post_list(request):
  if request.method == 'GET':
    posts = Post.objects.all().order_by('-created_at')
    return render(request, {'posts': posts})
