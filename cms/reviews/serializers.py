from rest_framework import serializers
from .models import PerformanceReview

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = ['id', 'employee', 'state', 'feedback', 'scheduled_date', 'manager_notes']
        read_only_fields = ['state']  
