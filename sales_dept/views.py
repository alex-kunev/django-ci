from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Lead


class LeadListView(ListView):
    model = Lead
    template_name = 'sales_dept/lead_list.html'
    context_object_name = 'leads'
    paginate_by = 10


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'sales_dept/lead_detail.html'
    context_object_name = 'lead'

