from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('bulletin/', views.bulletin_index),
    path('bulletin/<int:post_pk>/', views.bulletin_post_detail),
    path('bulletin/<int:post_pk>/comment/', views.bulletin_comment_list),
    path('bulletin/comment/', views.bulletin_comment_create),
    path('bulletin/comment/<int:comment_pk>/', views.bulletin_comment_detail),
    path('consumer/', views.consumer_index),
    path('consumer/<int:post_pk>/', views.consumer_post_detail),
    path('consumer/<int:post_pk>/buyit/', views.consumer_buyit),
    path('consumer/<int:post_pk>/dontbuyit/', views.consumer_dontbuyit),
    path('consumer/<int:post_pk>/comment/', views.consumer_comment_list),
    path('consumer/comment/', views.consumer_comment_create),
    path('consumer/comment/<int:comment_pk>/', views.consumer_comment_detail),
    path('challenge/', views.challenge_index),
    path('challenge/<int:post_pk>/', views.challenge_post_detail),
    path('challenge/<int:post_pk>/comment/', views.challenge_comment_list),
    path('challenge/comment/', views.challenge_comment_create),
    path('challenge/comment/<int:comment_pk>/', views.challenge_comment_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)