from django.db import models
from companies.models import Company

class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def number_of_employees(self):
        return self.employees.count()

    def number_of_projects(self):
        return self.projects.count()

    def __str__(self):
        return f"{self.name} ({self.company.name})"
