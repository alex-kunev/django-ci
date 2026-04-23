from django.contrib import admin
from .models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('title',)

