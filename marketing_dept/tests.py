from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from .models import Campaign


class CampaignModelTest(TestCase):
    """Test the Campaign model"""

    def setUp(self):
        """Create a test campaign"""
        self.campaign = Campaign.objects.create(
            title="Summer Sale",
            budget=Decimal("5000.00"),
            active=True
        )

    def test_campaign_creation(self):
        """Test creating a campaign"""
        self.assertEqual(self.campaign.title, "Summer Sale")
        self.assertEqual(self.campaign.budget, Decimal("5000.00"))
        self.assertTrue(self.campaign.active)

    def test_campaign_str_representation(self):
        """Test the string representation of a campaign"""
        self.assertEqual(str(self.campaign), "Summer Sale")

    def test_campaign_default_active(self):
        """Test that campaigns are active by default"""
        campaign = Campaign.objects.create(
            title="Test Campaign",
            budget=Decimal("1000.00")
        )
        self.assertTrue(campaign.active)


class CampaignViewTest(TestCase):
    """Test the Campaign views"""

    def setUp(self):
        """Create test campaigns"""
        self.campaign1 = Campaign.objects.create(
            title="Summer Sale",
            budget=Decimal("5000.00"),
            active=True
        )
        self.campaign2 = Campaign.objects.create(
            title="Winter Promotion",
            budget=Decimal("3000.00"),
            active=False
        )

    def test_campaign_list_view(self):
        """Test the campaign list view"""
        response = self.client.get(reverse('marketing_dept:campaign_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Summer Sale")
        self.assertContains(response, "Winter Promotion")
        self.assertTemplateUsed(response, 'marketing_dept/campaign_list.html')

    def test_campaign_detail_view(self):
        """Test the campaign detail view"""
        response = self.client.get(
            reverse('marketing_dept:campaign_detail', args=[self.campaign1.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Summer Sale")
        self.assertContains(response, "5000.00")
        self.assertTemplateUsed(response, 'marketing_dept/campaign_detail.html')

    def test_campaign_detail_view_nonexistent(self):
        """Test accessing a nonexistent campaign"""
        response = self.client.get(
            reverse('marketing_dept:campaign_detail', args=[999])
        )
        self.assertEqual(response.status_code, 404)

    def test_campaign_active_status(self):
        """Test campaign active/inactive display"""
        response = self.client.get(reverse('marketing_dept:campaign_list'))
        self.assertContains(response, "Active")
        self.assertContains(response, "Inactive")

