from django.contrib import admin
from django.contrib.auth.models import User
from user.models import Profile
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)