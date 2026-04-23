from django.urls import path
from .views import CampaignListView, CampaignDetailView

app_name = 'marketing_dept'

urlpatterns = [
    path('', CampaignListView.as_view(), name='campaign_list'),
    path('<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
]
