from django.urls import path
from . import views

urlpatterns = [
  path('user_delete/', views.delete_user),
  path('update-user-type/', views.update_user_type),
]