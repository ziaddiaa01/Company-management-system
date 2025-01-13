from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .models import Department
from .serializers import DepartmentSerializer
from users.permissions import IsAdmin, IsManagerOrReadOnly

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.user.role == 'Admin':
            return [IsAdmin()]
        elif self.request.user.role == 'Manager':
            return [IsManagerOrReadOnly()]
        return [IsAuthenticated()]

    def get_queryset(self):
        """
        Limit data to the Manager's company.
        """
        user = self.request.user
        if user.role == 'Manager':
            return self.queryset.filter(company=user.company)
        return self.queryset
