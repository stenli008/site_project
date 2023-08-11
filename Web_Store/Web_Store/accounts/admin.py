from django.contrib import admin

from Web_Store.accounts.models import CustomerUser
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
    actions = ['activate_users', 'deactivate_users']

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "Activate selected users"

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_users.short_description = "Deactivate selected users"


admin.site.register(CustomerUser, UserAdmin)
