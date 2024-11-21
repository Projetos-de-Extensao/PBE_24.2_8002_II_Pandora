from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  #
    path('feedback/', include('feedback.urls')),
    path('SWOT/', include('SWOT.urls')),
    path('auth/', obtain_auth_token, name='api_token_authentication'),
   
]



