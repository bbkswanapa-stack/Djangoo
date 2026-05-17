from django.contrib import admin
from home.models import Student

# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'DOB', 'number', 'is_active']
    search_fields = ['name', 'DOB']
    list_filter = ['is_active']