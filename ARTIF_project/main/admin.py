# from django.contrib import admin
# from .models import artif_start
# # Register your models here.
# admin.site.register(artif_start)

# dappx/admin.py
from django.contrib import admin
from main.models import UserProfileInfo, User
# Register your models here.
admin.site.register(UserProfileInfo)