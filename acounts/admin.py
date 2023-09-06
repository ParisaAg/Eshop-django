from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','is_active','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.
admin.site.register(Account,AccountAdmin)