# From Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# From Apps
from .models import User, Contact


UserAdmin.list_display += ("following_count", "followers_count", "show_profile")
UserAdmin.fieldsets[1][1]["fields"] = ('first_name', 'last_name', 'email', 'profile', 'biography')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Contact)
