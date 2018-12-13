from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import FormularioContato, FormularioPost


def listar_contatos(request,id):
    contatos = Usuario.objects.all()
    return render(request, 'contatos.html', {'contatos' : contatos},{'id' : id})


def novo_contato(request):
    form = FormularioContato(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'formulario_contato.html', {'form' : form})

def atualizar_contato(request, id):

    contato = get_object_or_404(Usuario, pk=id)
    form = FormularioContato(request.POST or None, instance = contato)

    if form.is_valid():
        form.save()
        return redirect('lista_contatos')

    return render(request,'formulario_contato.html', {'form' : form})


def postagens(request, id):
    formPost = FormularioPost(request.POST or None)
    usuarioLogado = get_object_or_404(Usuario, pk=id)
    posts = Post.objects.all()
    posts = Post.objects.filter(autor=usuarioLogado.id)
    print(posts)

    busca = request.GET.get('busca')

    if busca:
        usuarios = Usuario.objects.all()
        usuarios = Usuario.objects.filter(nome__icontains=busca)
        return render(request, 'contatos.html', {'contatos': usuarios}, {'id' : id})

    if formPost.is_valid():
        post = formPost.save(commit=False)
        post.autor = usuarioLogado
        post.save()
        return redirect('postagens', usuarioLogado.id)


    return render(request, 'index.html', {'form': formPost, 'usuarioLogado' : usuarioLogado , 'posts': posts})

def excluir_postagem(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('postagens',UsuarioLoged().id)




def login(request):
    usuarioLogado = UsuarioLogado.objects.all()
    if len(usuarioLogado) > 0:
        return redirect('postagens',usuarioLogado[0].usuario.id)

    else:
        usuarioLogado = UsuarioLogado()
        email = request.GET.get('email')
        senha = request.GET.get('senha')


        if email and senha:
            usuario = Usuario.objects.all()
            usuario = Usuario.objects.filter(email = email, senha = senha)
            usuarioLogado.usuario = usuario[0]
            usuarioLogado.save()

            return redirect('postagens',usuarioLogado.usuario.id)

    return render(request,'login.html')

def logout(request):
    usuarioLogado = UsuarioLogado.objects.all()
    for user in usuarioLogado:
        user.delete()

    return redirect('login')

def convidar(request,id):
    usuarioLogado = UsuarioLoged()
    convite = Convite()
    convite.solicitante = usuarioLogado
    convite.convidado = Usuario.objects.get(id = id)
    if convite.convidado in usuarioLogado.amigos.all() or convite in Convite.objects.all():
        pass
        #messages.info(request, 'Vocês já são amigos!')
    else:
        convite.save()

    return redirect('postagens',usuarioLogado.id)

def verAmigos(request):
    usuarioLogado = UsuarioLoged()

    convite = Convite.objects.all()
    convite =Convite.objects.filter(convidado_id = usuarioLogado.id)

    amigos = usuarioLogado.amigos.all()

    busca = request.GET.get('busca')

    if busca:
        usuarios = Usuario.objects.all()
        usuarios = Usuario.objects.filter(nome__icontains=busca)
        return render(request, 'contatos.html', {'contatos': usuarios}, {'id': id})

    return render(request,'amigos.html', {'convites' : convite , 'amigos' : amigos})

def aceitarPedido(request,id):
    usuarioLogado = UsuarioLoged()
    convite = Convite.objects.get(id = id)

    amigo = convite.solicitante

    usuarioLogado.amigos.add(amigo)
    amigo.amigos.add(usuarioLogado)

    convite.delete()

    return redirect('amigos')



def visitarPerfil(request, id_perfil):
    perfil = Usuario.objects.get(id=id_perfil)
    posts = Post.objects.filter(autor=perfil.id)

    return render(request, 'perfil.html', {'perfil': perfil, 'posts': posts})



def UsuarioLoged():
    usuarioLogado = UsuarioLogado.objects.all()
    if len(usuarioLogado) > 0:
        usuarioLogado = usuarioLogado[0].usuario



    return usuarioLogado
