from django.forms import ModelForm, widgets, Textarea, PasswordInput
from .models import *

class FormularioContato(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','sobrenome','email', 'senha']
        widgets = {'senha': PasswordInput}

class FormularioPost(ModelForm):
    class Meta:
        model = Post
        fields = ['texto']
        widgets = {
            'texto': Textarea,
        }