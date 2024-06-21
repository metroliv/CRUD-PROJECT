from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'phone', 'location', 'hobby')
    search_fields = ('name', 'email', 'location')

admin.site.register(Student, StudentAdmin)
