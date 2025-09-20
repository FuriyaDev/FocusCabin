from django.contrib import admin

# Register your models here.

from .models import Notification

@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'message']
    search_fields = ['user']
    ordering = ['-created_at']
