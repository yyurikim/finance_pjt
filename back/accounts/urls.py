from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('user_delete/', views.delete_user),
  path('profile/', views.profile, name='profile'),
  path('update-user-type/', views.update_user_type),
  path('update-user-info/', views.update_user_info),
  path('update-user-goal/', views.update_user_goal),
  path('user-goal-view/', views.user_goal_view),
]
