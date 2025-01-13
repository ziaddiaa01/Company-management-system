from django.test import TestCase
from employees.serializers import EmployeeSerializer
from employees.models import Employee
from companies.models import Company
from departments.models import Department

class EmployeeSerializerTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="TechCorp")
        self.department = Department.objects.create(name="Engineering", company=self.company)
        self.employee_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "company": self.company.id,
            "department": self.department.id,
            "designation": "Developer"
        }

    def test_valid_employee_serializer(self):
        serializer = EmployeeSerializer(data=self.employee_data)
        self.assertTrue(serializer.is_valid())
