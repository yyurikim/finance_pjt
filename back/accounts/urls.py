from django.urls import path
from . import views

urlpatterns = [
  path('user_delete/', views.delete_user),
]