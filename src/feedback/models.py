from django.db import models
from django.utils import timezone

class PlatformFeedback(models.Model):
    CATEGORY_TYPES = [
        ('suggestion', 'Suggestion for Improvement'),
        ('technical_issue', 'Technical Issue'),
        ('general_feedback', 'General Feedback'),
    ]
    
    category = models.CharField(max_length=60, choices=CATEGORY_TYPES)
    submission_date = models.DateTimeField(auto_now_add=True)
    submission_time = models.TimeField(default=timezone.now)  # Adicionando valor default
    description = models.TextField()
    reporter = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.reporter} - {self.category}'
