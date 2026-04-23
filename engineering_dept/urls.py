from django.urls import path
from .views import EngineerListView, EngineerDetailView

app_name = 'engineering_dept'

urlpatterns = [
    path('', EngineerListView.as_view(), name='engineer_list'),
    path('<int:pk>/', EngineerDetailView.as_view(), name='engineer_detail'),
]
