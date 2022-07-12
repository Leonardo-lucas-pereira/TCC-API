from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from api.views import ListaUsuarios, UsuariosViewSet


router = routers.DefaultRouter()
router.register('cadastrar_usuario', UsuariosViewSet, basename='Cadastrar Usuário')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastrar_usuario/', ListaUsuarios.as_view())
]
