from django import forms
from . import models
from .models.documento import Tipo
from .models.choices import TIPODOMEIO_CHOICES,LOGRADOURO_CHOICES
from django.core import validators
class ComunicanteForm(forms.ModelForm):
    
    class Meta:
        model = models.Comunicante
        fields = ('nome',)
        widgets = {
           'nome': forms.TextInput(attrs={"class": "form-control mb-2"}),
        }

        
        
class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = ('tipo','forma')
        widgets = {
            'tipo': forms.Select(attrs={"class": "form-control"},choices=TIPODOMEIO_CHOICES),
            'forma': forms.TextInput(attrs={"class": "form-control mb-2"})
        }
    

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = models.Endereco 
        fields = '__all__'
        widgets = {
            'tipo_de_logradouro': forms.Select(attrs={"class": "form-control mb-2"},choices=LOGRADOURO_CHOICES),
            'complemento': forms.TextInput(attrs={"class": "form-control mb-2"}),
            'numero': forms.NumberInput(attrs={"class": "form-control mb-2"}),
            'logradouro': forms.TextInput(attrs={"class": "form-control mb-2"}),
            'cidade':forms.Select(attrs={"class": "form-control mb-2"}),
            'bairro':forms.Select(attrs={"class": "form-control mb-2"}),
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
            'descricao_situacao': forms.Textarea(attrs={"class": "form-control mb-2 "}),
            'nomevitimas': forms.Textarea(attrs={"class": "form-control  mb-2"}),
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
        exclude = ['enderecos']

    def __init__(self,*args, **kwargs):
        super(VitimaForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'
            
class ArquivoForm(forms.ModelForm):
    class Meta:
        model = models.Arquivo
        fields = ['upload']
        widgets = {
            'upload': forms.ClearableFileInput(attrs={'multiple': True}),
        }
    
    def __init__(self,*args, **kwargs):
        super(ArquivoForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'

class VitimaToOcorrenciaForm(forms.Form):
    vitima = forms.CharField(max_length=100)
    def __init__(self,*args, **kwargs):
        self.denuncia = kwargs.pop('denuncia')
        super(VitimaToOcorrenciaForm, self).__init__(*args, **kwargs)
        self.fields['vitima'].label = "Digite o nome da vitima ligada a essa denuncia"

        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'
            new_field.field.widget.attrs['list'] = 'datalistVitimas'

    def clean(self):
        vitima = self.cleaned_data['vitima']
        nova_vitima = ''
        if models.Ocorrencia.objects.all().filter(denuncia=self.denuncia):
            ocorrencia = models.Ocorrencia.objects.get(denuncia=self.denuncia)
            if ocorrencia.vitimas.all():
                for atual in ocorrencia.vitimas.all():
                    if atual.nome == vitima:
                        self.add_error('vitima', 'Vitima ja está nessa denuncia')
                    else:
                        filtro = models.Vitima.objects.filter(nome=vitima)
                        if not filtro:
                            nova_vitima = models.Vitima.objects.create(nome=vitima)
                        else:
                            vitimas = models.Vitima.objects.get(nome=vitima)
                            ocorrencia.vitimas.add(vitimas)
            else:
                nova_vitima = models.Vitima.objects.create(nome=vitima)
                ocorrencia.vitimas.add(nova_vitima)

        else:
            if vitima != '':
                denuncia = models.Denuncia.objects.get(id=self.denuncia)
                vitimas = models.Vitima.objects.create(nome=vitima)
                ocorrencia = models.Ocorrencia.objects.create(denuncia=denuncia)
                ocorrencia.vitimas.add(vitimas)
        return self.cleaned_data