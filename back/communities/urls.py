from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('post/<int:post_pk>/', views.post_detail),
    path('post/<int:post_pk>/comment/', views.comment_detail),
]