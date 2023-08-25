# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

class CustomUserAdmin(UserAdmin):
    # Customize the admin view as needed
    list_display = ('username', 'email', 'first_name', 'last_name', 'profilePhoto')
    # fields = [
    #     'username',
    #     'password',
    #     'email',
    #     'first_name',
    #     'last_name',
    #     'profilePhoto'
    # ]

# Register the custom user model with the admin site
admin.site.register(CustomUserModel, CustomUserAdmin)

