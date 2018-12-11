from datetime import datetime

from django.db import models

# Create your models here.



class Usuario(models.Model):
    nome = models.CharField(max_length= 30)
    sobrenome = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    senha = models.CharField(max_length=50, default='123')

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Post(models.Model):

    texto = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(default=datetime.now())
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='postagens')

    class meta:
        ordering = ['-data_publicacao']