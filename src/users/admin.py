from django.contrib import admin

# Register your models here.

from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username','phone_number','is_block','is_verified']
    search_fields = ('username','phone_number', 'first_name', 'last_name')
    list_editable = ['is_block']
    list_filter = ['created_at']
    ordering = ['-created_at']
