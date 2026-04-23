from django.contrib import admin
from .models import Engineer


@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('name', 'email')

