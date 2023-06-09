from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm


app_name = 'users'
urlpatterns=[
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/<int:user_id>/', views.view_profile, name='profile'),
    path('profile/follow/<int:profile_id>', views.follow, name='follow'),
    path('profile/unfollow/<int:profile_id>', views.unfollow, name='unfollow'),
]