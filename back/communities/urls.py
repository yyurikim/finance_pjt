from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('post/<int:post_pk>/', views.post_detail),
    # path('post/<int:post_pk>/comment/', views.comment_detail),
]