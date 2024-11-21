from rest_framework import viewsets
from .models import PlatformFeedback, FeedbackAnalysis
from .serializers import PlatformFeedbackSerializer, FeedbackAnalysisSerializer

class PlatformFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PlatformFeedback.objects.all()
    serializer_class = PlatformFeedbackSerializer

class FeedbackAnalysisViewSet(viewsets.ModelViewSet):
    queryset = FeedbackAnalysis.objects.all()
    serializer_class = FeedbackAnalysisSerializer
