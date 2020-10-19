from django import forms
from .models import Endereco,choices,Ocorrencia,Denuncia,Comunicante
from .models.documento import Tipo
from .models.choices import TIPODOMEIO_CHOICES

class ComunicanteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # tipo =  forms.Select(attrs={'class': 'form-control'},choices=TIPODOMEIO_CHOICES)
    # forma = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # escolha =  forms.Select(attrs={'class': 'form-control'},choices=Tipo.choices())
    # valor = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Comunicante
        
        fields = ('nome',)


