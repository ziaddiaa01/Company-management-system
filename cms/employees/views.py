from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer
from users.permissions import IsAdmin, IsManagerOrReadOnly, IsEmployeeReadOnly
from rest_framework.exceptions import PermissionDenied

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        """
        Assign permissions based on user role.
        """
        if self.request.user.role == 'Admin':
            return [IsAdmin()]
        elif self.request.user.role == 'Manager':
            return [IsManagerOrReadOnly()]
        elif self.request.user.role == 'Employee':
            return [IsEmployeeReadOnly()]
        return [IsAuthenticated()]

    def get_queryset(self):
        """
        Limit the queryset based on user role.
        - Admin: Can view all employees.
        - Manager: Can view employees in their company.
        - Employee: Can only view their own data.
        """
        user = self.request.user
        if user.role == 'Admin':
            return Employee.objects.all()
        elif user.role == 'Manager':
            return Employee.objects.filter(company=user.company)
        elif user.role == 'Employee':
            return Employee.objects.filter(id=user.id)
        raise PermissionDenied("You do not have permission to view this data.")

    def perform_create(self, serializer):
        """
        Validate that the department belongs to the selected company.
        """
        employee = serializer.save()
        if employee.department.company != employee.company:
            raise Exception("The department does not belong to the selected company.")
