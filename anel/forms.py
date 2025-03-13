from django import forms
from .models import Anel


class AnelForm(forms.ModelForm):
    class Meta:
        model = Anel
        fields = ['nome', 'poder', 'portador', 'forjadoPor', 'imagem']
