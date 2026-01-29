from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = (
        'email',
        'username',
        'full_name',
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_filter = (
        'is_staff',
        'is_active',
    )
    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )
    ordering = ('-date_joined',)

    fieldsets = (
        ('Основное', {
            'fields': (
                'email',
                'password',
            )
        }),
        ('Персональные данные', {
            'fields': (
                'username',
                'first_name',
                'last_name',
                'patronymic',
                'avatar',
                'bio',
                'phone',
            )
        }),
        ('Права доступа', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Даты', {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )

    readonly_fields = (
        'date_joined',
        'last_login',
    )
