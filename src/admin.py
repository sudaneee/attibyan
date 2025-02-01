from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'category', 'date_applied', 'status')  # Show in list view
    list_filter = ('category', 'gender', 'date_applied', 'status')  # Filter sidebar
    search_fields = ('full_name', 'email', 'phone')  # Search bar
    readonly_fields = ('date_applied',)  # Make read-only
    ordering = ('-date_applied',)  # Newest applications first
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone', 'dob', 'gender', 'profile_picture')
        }),
        ('Application Details', {
            'fields': ('category', 'optional_courses', 'preferred_time', 'motivation', 'certificates')
        }),
        ('Status & Admin Control', {
            'fields': ('status', 'date_applied')
        }),
    )

admin.site.register(Application, ApplicationAdmin)
