from rest_framework import viewsets
from .models import UserProfile  
from .serializers import UserProfileSerializer  
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  

def user_view(request):
    return render(request, 'user/user.html')  
