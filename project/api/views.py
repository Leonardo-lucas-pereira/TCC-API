from rest_framework import viewsets, generics


from api.models import Usuario
from api.serializers import UsuarioSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    serializer_class = UsuarioSerializer