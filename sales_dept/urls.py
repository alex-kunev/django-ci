from django.urls import path
from .views import LeadListView, LeadDetailView

app_name = 'sales_dept'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
]
