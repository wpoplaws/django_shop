from django.contrib import admin
from .models import Profile, Camping


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


@admin.register(Camping)
class CampingAdmin(admin.ModelAdmin):
    list_display = ['name']
