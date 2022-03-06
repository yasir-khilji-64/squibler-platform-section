from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = (
        'email',
        'gravatar_url',
        'is_active',
        'is_admin',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_admin',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(get_user_model(), UserAdmin)
