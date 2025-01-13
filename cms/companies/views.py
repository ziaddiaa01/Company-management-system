from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .models import Company
from .serializers import CompanySerializer
import logging

logger = logging.getLogger(__name__)

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        company = serializer.save()
        logger.info(f"Company {company.name} created by {self.request.user.username}")
