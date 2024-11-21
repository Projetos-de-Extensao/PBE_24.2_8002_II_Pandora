# serializers.py

from rest_framework import serializers
from .models import PlatformFeedback, FeedbackAnalysis

class PlatformFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformFeedback
        fields = ['category', 'submission_date', 'description', 'requester']

class FeedbackAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackAnalysis
        fields = ['feedback', 'notes', 'status', 'name', 'analysis_date']
