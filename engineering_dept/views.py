from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Engineer


class EngineerListView(ListView):
    model = Engineer
    template_name = 'engineering_dept/engineer_list.html'
    context_object_name = 'engineers'
    paginate_by = 10


class EngineerDetailView(DetailView):
    model = Engineer
    template_name = 'engineering_dept/engineer_detail.html'
    context_object_name = 'engineer'

