from django.contrib import admin
from .models import Account


class AccountDisplay(admin.ModelAdmin):
    list_display = ('name', 'user_email', 'username', 'password')


admin.site.register(Account, AccountDisplay)

