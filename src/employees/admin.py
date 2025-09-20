from django.contrib import admin

# Register your models here.

from .models import Employee

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'position']
    search_fields = ('user', 'position')
    ordering = ['-created_at']
