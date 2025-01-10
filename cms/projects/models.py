from django.db import models
from departments.models import Department
from companies.models import Company
from employees.models import Employee

class Project(models.Model):
    company = models.ForeignKey(Company, related_name='projects', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name
