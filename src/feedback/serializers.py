from rest_framework import serializers
from .models import PlatformFeedback

class PlatformFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformFeedback
        fields = ['id', 'category', 'submission_date', 'submission_time', 'description', 'reporter']
