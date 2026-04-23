from django.test import TestCase
from django.urls import reverse
from .models import Lead


class LeadModelTest(TestCase):
    """Test the Lead model"""

    def setUp(self):
        """Create a test lead"""
        self.lead = Lead.objects.create(
            company="Acme Corp",
            contact_name="Alice Johnson",
            status="new"
        )

    def test_lead_creation(self):
        """Test creating a lead"""
        self.assertEqual(self.lead.company, "Acme Corp")
        self.assertEqual(self.lead.contact_name, "Alice Johnson")
        self.assertEqual(self.lead.status, "new")

    def test_lead_str_representation(self):
        """Test the string representation of a lead"""
        expected_str = f"{self.lead.contact_name} from {self.lead.company}"
        self.assertEqual(str(self.lead), expected_str)

    def test_lead_status_choices(self):
        """Test that lead status choices work correctly"""
        self.assertEqual(self.lead.status, "new")
        self.lead.status = "contacted"
        self.lead.save()
        self.assertEqual(self.lead.status, "contacted")
        self.lead.status = "converted"
        self.lead.save()
        self.assertEqual(self.lead.status, "converted")


class LeadViewTest(TestCase):
    """Test the Lead views"""

    def setUp(self):
        """Create test leads"""
        self.lead1 = Lead.objects.create(
            company="Acme Corp",
            contact_name="Alice Johnson",
            status="new"
        )
        self.lead2 = Lead.objects.create(
            company="Tech Inc",
            contact_name="Bob Smith",
            status="converted"
        )

    def test_lead_list_view(self):
        """Test the lead list view"""
        response = self.client.get(reverse('sales_dept:lead_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice Johnson")
        self.assertContains(response, "Bob Smith")
        self.assertTemplateUsed(response, 'sales_dept/lead_list.html')

    def test_lead_detail_view(self):
        """Test the lead detail view"""
        response = self.client.get(
            reverse('sales_dept:lead_detail', args=[self.lead1.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice Johnson")
        self.assertContains(response, "Acme Corp")
        self.assertTemplateUsed(response, 'sales_dept/lead_detail.html')

    def test_lead_detail_view_nonexistent(self):
        """Test accessing a nonexistent lead"""
        response = self.client.get(
            reverse('sales_dept:lead_detail', args=[999])
        )
        self.assertEqual(response.status_code, 404)

    def test_lead_status_display(self):
        """Test that different lead statuses are displayed correctly"""
        response = self.client.get(reverse('sales_dept:lead_list'))
        self.assertContains(response, "New")
        self.assertContains(response, "Converted")

