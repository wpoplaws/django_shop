from django.contrib import admin
from .models import Profile, Camping, FriendRequest


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'id', 'slug']


@admin.register(Camping)
class CampingAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'id']
