from django.contrib import admin
from .models import University, Student
# Register your models here.

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']