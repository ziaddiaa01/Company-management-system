from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Company
from .serializers import CompanySerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrReadOnly

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

