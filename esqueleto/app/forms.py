from django import forms
from . import models
from .models.documento import Tipo
from .models.choices import TIPODOMEIO_CHOICES,LOGRADOURO_CHOICES

class ComunicanteForm(forms.ModelForm):
    
    class Meta:
        model = models.Comunicante
        fields = ('nome',)
        widgets = {
           'nome': forms.TextInput(attrs={"class": "form-control "}),
        }

        
        
class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = ('tipo','forma')
        widgets = {
            'tipo': forms.Select(attrs={"class": "form-control"},choices=TIPODOMEIO_CHOICES),
            'forma': forms.TextInput(attrs={"class": "form-control"})
        }
    

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = models.Endereco 
        fields = '__all__'
        widgets = {
            'tipo_de_logradouro': forms.Select(attrs={"class": "form-control"},choices=LOGRADOURO_CHOICES),
            'complemento': forms.TextInput(attrs={"class": "form-control"}),
            'numero': forms.NumberInput(attrs={"class": "form-control"}),
            'logradouro': forms.TextInput(attrs={"class": "form-control"}),
            'cidade':forms.Select(attrs={"class": "form-control"}),
            'bairro':forms.Select(attrs={"class": "form-control"}),
        }
        

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = models.Documento 
        fields = ('escolha','valor',)
        widgets = {
            'escolha': forms.Select(attrs={"class": "form-control"},choices=Tipo.choices()),
            'valor': forms.NumberInput(attrs={"class": "form-control"}),

            
        }
        
class DenunciaForm(forms.ModelForm):
     class Meta:
        model = models.Denuncia 
        fields = ('descricao_situacao','nomevitimas')
        widgets = {
            'horario': forms.DateTimeInput(attrs={"class": "form-control col-4","type": "datetime-local"}),
            'descricao_situacao': forms.Textarea(attrs={"class": "form-control "}),
            'nomevitimas': forms.Textarea(attrs={"class": "form-control  "}),
        }

class DireitoForm(forms.ModelForm):
    class Meta:
        model = models.Direito
        fields = ('nome_direito',)
        widgets = {
            'nome_direito': forms.TextInput(attrs={"class": "form-control col-4"}),
        }
class AnotacaoForm(forms.ModelForm):
    class Meta:
        model = models.Anotacao
        fields = ('titulo','descricao')
        


    def __init__(self,*args, **kwargs):
        super(AnotacaoForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'
        

class VitimaForm(forms.ModelForm):
    class Meta:
        model = models.Vitima
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(VitimaForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'
            