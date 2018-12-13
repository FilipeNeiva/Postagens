from django.forms import ModelForm, widgets, Textarea
from .models import *

class FormularioContato(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','sobrenome','email','senha']

class FormularioPost(ModelForm):
    class Meta:
        model = Post
        fields = ['texto']
        widgets = {
            'texto': Textarea,
        }