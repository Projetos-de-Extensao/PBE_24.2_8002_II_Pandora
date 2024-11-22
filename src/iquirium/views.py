from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserApiView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Aqui você pode retornar uma lista de usuários ou dados desejados
        return Response({"message": "Usuário autenticado com sucesso"})
