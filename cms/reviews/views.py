from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import PerformanceReview
from .serializers import PerformanceReviewSerializer
import logging
logger = logging.getLogger(__name__)


class PerformanceReviewViewSet(ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

    @action(detail=True, methods=['post'])
    def schedule(self, request, pk=None):
        """Transition: Pending Review → Review Scheduled"""
        review = self.get_object()
        review.schedule_review()
        logger.info(f"Review {review.id} scheduled for employee {review.employee.name}")
        review.scheduled_date = request.data.get('scheduled_date')
        review.save()
        return Response({'status': 'Review scheduled successfully'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def provide_feedback(self, request, pk=None):
        """Transition: Review Scheduled → Feedback Provided"""
        review = self.get_object()
        feedback = request.data.get('feedback')
        if not feedback:
            return Response({'error': 'Feedback is required'}, status=status.HTTP_400_BAD_REQUEST)
        review.provide_feedback(feedback=feedback)
        review.save()
        return Response({'status': 'Feedback provided successfully'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def submit_for_approval(self, request, pk=None):
        """Transition: Feedback Provided → Under Approval"""
        review = self.get_object()
        review.submit_for_approval()
        review.save()
        return Response({'status': 'Review submitted for approval'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Transition: Under Approval → Review Approved"""
        try:
            review = self.get_object()
        except PerformanceReview.DoesNotExist:
            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    
        manager_notes = request.data.get('manager_notes')
        if not manager_notes:
            return Response({'error': 'Manager notes are required'}, status=status.HTTP_400_BAD_REQUEST)
    
        review.approve_review(manager_notes=manager_notes)
        review.save()
        return Response({'status': 'Review approved successfully'}, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """Transition: Under Approval → Review Rejected"""
        review = self.get_object()
        manager_notes = request.data.get('manager_notes')
        review.reject_review(manager_notes=manager_notes)
        review.save()
        return Response({'status': 'Review rejected successfully'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def resubmit_feedback(self, request, pk=None):
        """Transition: Review Rejected → Feedback Provided"""
        review = self.get_object()
        feedback = request.data.get('feedback')
        if not feedback:
            return Response({'error': 'Feedback is required'}, status=status.HTTP_400_BAD_REQUEST)
        review.resubmit_feedback(feedback=feedback)
        review.save()
        return Response({'status': 'Feedback resubmitted successfully'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Admin':
            return PerformanceReview.objects.all()
        elif user.role == 'Manager':
            return PerformanceReview.objects.filter(employee__department__company=user.company)
        elif user.role == 'Employee':
            return PerformanceReview.objects.filter(employee=user)
        return PerformanceReview.objects.none()
