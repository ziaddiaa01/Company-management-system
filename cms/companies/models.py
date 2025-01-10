from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    
    def number_of_departments(self):
        return self.departments.count()

    def number_of_employees(self):
        return sum(department.number_of_employees() for department in self.departments.all())

    def number_of_projects(self):
        return sum(department.number_of_projects() for department in self.departments.all())

    def __str__(self):
        return self.name
