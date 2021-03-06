"""formularios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contatos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>', postagens, name = "postagens"),
    path('contatos', listar_contatos, name = "lista_contatos"),
    path('adicionar', novo_contato, name = "adicionar_contato"),
    path('atualizar/<int:id>/', atualizar_contato, name = "atualizar_contato"),
    path('logout/',logout,name="logout"),
    path('convidar/<int:id>/', convidar, name="convidar"),
    path('',login, name = 'login'),
    path('amigos/', verAmigos, name= "amigos"),
    path('amigos/<int:id>/aceitar', aceitarPedido, name='aceitar'),
    path('perfil/<int:id_perfil>', visitarPerfil, name='perfil'),
    path('excluir_postagem/<int:id>/',excluir_postagem,name= 'excluir_postagem'),

]
