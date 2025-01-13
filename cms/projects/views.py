from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer
from users.permissions import IsAdmin, IsManagerOrReadOnly

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.user.role == 'Admin':
            return [IsAdmin()]
        elif self.request.user.role == 'Manager':
            return [IsManagerOrReadOnly()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        project = serializer.save()
        for employee in project.assigned_employees.all():
            if employee.company != project.company:
                raise ValidationError(f"Employee {employee.name} does not belong to the same company as the project.")
