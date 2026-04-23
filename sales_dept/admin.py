from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'company', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('contact_name', 'company')

