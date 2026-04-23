from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Campaign


class CampaignListView(ListView):
    model = Campaign
    template_name = 'marketing_dept/campaign_list.html'
    context_object_name = 'campaigns'
    paginate_by = 10


class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'marketing_dept/campaign_detail.html'
    context_object_name = 'campaign'

