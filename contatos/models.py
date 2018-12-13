from datetime import datetime

from django.db import models

# Create your models here.



class Usuario(models.Model):
    nome = models.CharField(max_length= 30)
    sobrenome = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    amigos = models.ManyToManyField('Usuario', related_name='amigos_usuario')
    senha = models.CharField(max_length=15)

    def convidar(self, user):
        convite = Convite.save(commit=False)
        convite.solicitante = self
        convite.solicitado = user
        convite.save()

    def __str__(self):
        return self.nome + ' ' + self.sobrenome



class Convite(models.Model):
    convidado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="convites_recebidos")
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="convites_enviados")

    def __str__(self):
        return self.solicitante.nome


class Post(models.Model):

    texto = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(default=datetime.now())
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='postagens')

    class meta:
        ordering = ['-data_publicacao']


class UsuarioLogado(models.Model):
    usuario = models.ForeignKey(Usuario , on_delete=models.CASCADE)