from django.test import TestCase
from django.urls import reverse


class DashboardViewTest(TestCase):
    """Test the Dashboard view"""

    def test_dashboard_view(self):
        """Test the dashboard view loads correctly"""
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')
        self.assertContains(response, "Dashboard")
        self.assertContains(response, "Project Overview")

    def test_dashboard_links(self):
        """Test that dashboard contains links to other apps"""
        response = self.client.get(reverse('dashboard:index'))
        self.assertContains(response, "engineering")
        self.assertContains(response, "marketing")
        self.assertContains(response, "sales")

    def test_dashboard_page_title(self):
        """Test that dashboard has correct page title"""
        response = self.client.get(reverse('dashboard:index'))
        self.assertIn('Dashboard', response.context['page_title'])

