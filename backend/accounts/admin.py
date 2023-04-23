from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from . import models

class UserAdminConfig(UserAdmin):
    
    search_fields = ('email', 'username', )
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-date_joined', )
    list_display = ('email', 'username',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}), 
        ('Permissions', {'fields': ('is_active', 'is_staff')}), 
        ('Info', {'fields': ('bio', 'rating', 'avatar', 'custom_url')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')
        }),  # <- this comma is fucking important
    )

admin.site.register(models.Profile, UserAdminConfig)
