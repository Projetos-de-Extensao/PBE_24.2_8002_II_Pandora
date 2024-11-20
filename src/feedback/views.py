from rest_framework import viewsets
from .models import PlatformFeedback
from .serializers import PlatformFeedbackSerializer

class PlatformFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PlatformFeedback.objects.all()
    serializer_class = PlatformFeedbackSerializer
