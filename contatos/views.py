from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import FormularioContato, FormularioPost


def listar_contatos(request):
    contatos = Usuario.objects.all()
    return render(request, 'contatos.html', {'contatos' : contatos})


def novo_contato(request):
    form = FormularioContato(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_contatos')

    return render(request, 'formulario_contato.html', {'form' : form})

def atualizar_contato(request, id):

    contato = get_object_or_404(Usuario, pk=id)
    form = FormularioContato(request.POST or None, instance = contato)

    if form.is_valid():
        form.save()
        return redirect('lista_contatos')

    return render(request,'formulario_contato.html', {'form' : form})


def postagens(request, id = None):
    if id == None:
        return render(request, 'login.html')

    else:
        formPost = FormularioPost(request.POST or None)
        usuarioLogado = get_object_or_404(Usuario, pk=id)

        if formPost.is_valid():
            post = formPost.save(commit=False)
            post.autor = usuarioLogado
            post.save()
            return redirect('postagens', usuarioLogado.id)

        return render(request, 'index.html', {'form': formPost}, {'usuarioLogado': usuarioLogado})
