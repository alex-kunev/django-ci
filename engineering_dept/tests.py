from django.test import TestCase
from django.urls import reverse
from .models import Engineer


class EngineerModelTest(TestCase):
    """Test the Engineer model"""

    def setUp(self):
        """Create a test engineer"""
        self.engineer = Engineer.objects.create(
            name="John Doe",
            email="john@example.com",
            role="Senior Developer"
        )

    def test_engineer_creation(self):
        """Test creating an engineer"""
        self.assertEqual(self.engineer.name, "John Doe")
        self.assertEqual(self.engineer.email, "john@example.com")
        self.assertEqual(self.engineer.role, "Senior Developer")

    def test_engineer_str_representation(self):
        """Test the string representation of an engineer"""
        expected_str = f"{self.engineer.name} ({self.engineer.role})"
        self.assertEqual(str(self.engineer), expected_str)

    def test_engineer_ordering(self):
        """Test that engineers are ordered by creation date (newest first)"""
        engineer2 = Engineer.objects.create(
            name="Jane Smith",
            email="jane@example.com",
            role="Junior Developer"
        )
        engineers = Engineer.objects.all()
        self.assertEqual(engineers[0], engineer2)
        self.assertEqual(engineers[1], self.engineer)


class EngineerViewTest(TestCase):
    """Test the Engineer views"""

    def setUp(self):
        """Create test engineers"""
        self.engineer1 = Engineer.objects.create(
            name="John Doe",
            email="john@example.com",
            role="Senior Developer"
        )
        self.engineer2 = Engineer.objects.create(
            name="Jane Smith",
            email="jane@example.com",
            role="Junior Developer"
        )

    def test_engineer_list_view(self):
        """Test the engineer list view"""
        response = self.client.get(reverse('engineering_dept:engineer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "Jane Smith")
        self.assertTemplateUsed(response, 'engineering_dept/engineer_list.html')

    def test_engineer_detail_view(self):
        """Test the engineer detail view"""
        response = self.client.get(
            reverse('engineering_dept:engineer_detail', args=[self.engineer1.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "john@example.com")
        self.assertTemplateUsed(response, 'engineering_dept/engineer_detail.html')

    def test_engineer_detail_view_nonexistent(self):
        """Test accessing a nonexistent engineer"""
        response = self.client.get(
            reverse('engineering_dept:engineer_detail', args=[999])
        )
        self.assertEqual(response.status_code, 404)

