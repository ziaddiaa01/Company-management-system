from django.db import models
from django_fsm import FSMField, transition
from employees.models import Employee
import logging
logger = logging.getLogger(__name__)


class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews')
    state = FSMField(default='Pending Review')  
    feedback = models.TextField(null=True, blank=True)  
    scheduled_date = models.DateTimeField(null=True, blank=True)  
    manager_notes = models.TextField(null=True, blank=True)  


    @transition(field=state, source='Pending Review', target='Review Scheduled')
    def schedule_review(self):
        logger.info(f"Review for {self.employee.name} scheduled.")
        pass

    @transition(field=state, source='Review Scheduled', target='Feedback Provided')
    def provide_feedback(self, feedback):
        """Record feedback after the review meeting."""
        logger.info(f"Review for {self.employee.name} scheduled.")
        self.feedback = feedback

    @transition(field=state, source='Feedback Provided', target='Under Approval')
    def submit_for_approval(self):
        """Submit feedback for managerial approval."""
        pass

    @transition(field=state, source='Under Approval', target='Review Approved')
    def approve_review(self, manager_notes):
        """Manager approves the performance review."""
        self.manager_notes = manager_notes

    @transition(field=state, source='Under Approval', target='Review Rejected')
    def reject_review(self, manager_notes):
        """Manager rejects the performance review for rework."""
        self.manager_notes = manager_notes

    @transition(field=state, source='Review Rejected', target='Feedback Provided')
    def resubmit_feedback(self, feedback):
        """Resubmit feedback after rejection."""
        self.feedback = feedback

    def __str__(self):
        return f"Review for {self.employee.name} - {self.state}"
