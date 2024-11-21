from django.db import models
from django.conf import settings

class PlatformFeedback(models.Model):
    category = models.CharField(
        choices=[
            ('suggestion', 'Suggestion for Improvement'),
            ('technical_issue', 'Technical Issue'),
            ('general_feedback', 'General Feedback'),
        ],
        max_length=60
    )
    submission_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name='Detailed Feedback')
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.requester.get_full_name()} {self.category}'


class FeedbackAnalysis(models.Model):
    feedback = models.ForeignKey(PlatformFeedback, on_delete=models.CASCADE)
    analysis_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(verbose_name='Analysis Notes')
    status = models.CharField(
        choices=[
            ('pending', 'Pending Review'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
        ],
        max_length=30
    )
    name = models.CharField(max_length=255, verbose_name="Analyst", blank=True, null=True)

    class Meta:
        verbose_name = "Feedback Analysis"
        verbose_name_plural = "Feedback Analyses"

    def __str__(self):
        analyst_name = self.name if self.name else "No Analyst Assigned"
        feedback_type = self.feedback.category
        requester_name = self.feedback.requester.get_full_name()
        return f'{analyst_name} / {feedback_type} / {requester_name}'

