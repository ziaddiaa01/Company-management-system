from django.db import models
from django_fsm import FSMField, transition

class PerformanceReview(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    state = FSMField(default='Pending Review')

    @transition(field=state, source='Pending Review', target='Review Scheduled')
    def schedule_review(self):
        pass

    @transition(field=state, source='Review Scheduled', target='Feedback Provided')
    def provide_feedback(self):
        pass

    @transition(field=state, source='Feedback Provided', target='Under Approval')
    def submit_for_approval(self):
        pass

    @transition(field=state, source='Under Approval', target='Review Approved')
    def approve_review(self):
        pass

    @transition(field=state, source='Under Approval', target='Review Rejected')
    def reject_review(self):
        pass

    @transition(field=state, source='Review Rejected', target='Feedback Provided')
    def resubmit_feedback(self):
        pass
