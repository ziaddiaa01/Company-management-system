from django.test import TestCase
from companies.models import Company

class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="TechCorp")

    def test_number_of_departments(self):
        self.assertEqual(self.company.number_of_departments(), 0)

    def test_number_of_employees(self):
        self.assertEqual(self.company.number_of_employees(), 0)
