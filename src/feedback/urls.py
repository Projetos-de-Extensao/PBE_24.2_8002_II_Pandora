from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatformFeedbackViewSet, FeedbackAnalysisViewSet

router = DefaultRouter()
router.register(r'platform-feedback', PlatformFeedbackViewSet)
router.register(r'feedback-analysis', FeedbackAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

