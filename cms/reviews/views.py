
from rest_framework.viewsets import ModelViewSet
from .models import PerformanceReview
from .serializers import PerformanceReviewSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrReadOnly

class PerformanceReviewViewSet(ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

