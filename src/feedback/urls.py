from django.urls import path, include
from rest_framework import routers
from .views import PlatformFeedbackViewSet

router = routers.DefaultRouter()
router.register(r'feedbacks', PlatformFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
