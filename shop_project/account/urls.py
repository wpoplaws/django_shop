from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls import url

from .views import (
    users_list,
    profile_view,
    send_friend_request,
    cancel_friend_request,
    accept_friend_request,
    delete_friend_request
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.main, name='main'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.users_list, name='user_list'),
    path('users/<slug:slug>/', views.profile_view, name='profile_view'),
    path('<slug:name>/', views.camping_detail, name="camping_detail"),
    path('users/friend-request/send/<id>/', views.send_friend_request, name="send_friend_request"),
    path('users/friend-request/cancel/<id>/', views.cancel_friend_request, name='cancel_friend_request'),
    path('users/friend-request/accept/<id>/', views.accept_friend_request, name='accept_friend_request'),
    path('users/friend-request/delete/<id>/', views.delete_friend_request, name='delete_friend_request'),
    path('users/friend-request/delete_friend/<id>/', views.delete_friend, name='delete_friend'),
    path('user/settings/', views.settings, name='settings'),


    # url(r'^friend-request/accept/(?P<id>[\w-]+)/$', accept_friend_request),
    # url(r'^friend-request/delete/(?P<id>[\w-]+)/$', delete_friend_request),

]
