from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserApiView
from rest_framework.routers import DefaultRouter

# Criação do roteador
router = DefaultRouter()
router.register(r'user', UserApiView, basename='user')

urlpatterns = [
    # URLs do Admin
    path('admin/', admin.site.urls),

    # URLs de outros aplicativos (não removi nenhuma URL)
    path('user/', include('user.urls')),  # Rota para o app 'user'
    path('user/api/user', include('user.urls')),
     path('user/api/', include('user.urls')), 
    path('feedback/', include('feedback.urls')),  # Rota para o app 'feedback'
    path('SWOT/', include('SWOT.urls')),  # Rota para o app 'SWOT'

    # Autenticação de Token
    path('auth/', obtain_auth_token, name='api_token_authentication'),

    # Incluindo as URLs do roteador (isso vai mapear a URL /api/user/)
    path('api/', include(router.urls)),
]
