from django.db import models
from django.contrib.auth.models import User

class Swot(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='swots',
        null=True,   
        blank=True  
    )
    strength = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    opportunity = models.CharField(max_length=100)
    threat = models.CharField(max_length=100)
    swot_analysis = models.CharField(max_length=100)
    last_analysis_date = models.DateTimeField(auto_now_add=True)
    analysis_period_days = models.IntegerField()
    completion_status = models.BooleanField()

    def check_completion(self):
        pass

    def create_swot(self):
        pass

    def fill_swot(self):
        pass

    def generate_swot_analysis(self):
        pass

    def view_analysis(self):
        pass

    def modify_analysis_period(self):
        pass

    def __str__(self):
        return f'{self.user.username if self.user else "Unassigned"}'
