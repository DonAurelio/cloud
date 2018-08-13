from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

from authentication.models import Account

class AccountAdmin(UserAdmin):
    list_display = (
        'email',
        'is_active',
        'is_superuser',
        'last_login')

    fieldsets = (
        (_('Personal info'), {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser','groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email',)
    list_filter = ('email',)
    ordering = ['email']
    
admin.site.register(Account,AccountAdmin)


