from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'user', views.UserProfileViewSet) 

urlpatterns = [
    path('user-api/token/', obtain_auth_token, name='user_token_auth'),
    
    path('api/', include(router.urls)),

]
