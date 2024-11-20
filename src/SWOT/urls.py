from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SwotViewSet

router = DefaultRouter()
router.register(r'Swot', SwotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
