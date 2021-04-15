from django import forms
from . import models
from .models.documento import Tipo
from .models.choices import TIPODOMEIO_CHOICES,LOGRADOURO_CHOICES
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group

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
            'tipo_de_logradouro': forms.Select(attrs={"class": "form-select mb-2"},choices=LOGRADOURO_CHOICES),
            'complemento': forms.TextInput(attrs={"class": "form-control mb-2"}),
            'numero': forms.NumberInput(attrs={"class": "form-control mb-2"}),
            'logradouro': forms.TextInput(attrs={"class": "form-control mb-2"}),
            'cidade':forms.Select(attrs={"class": "form-select mb-2"}),
            'bairro':forms.Select(attrs={"class": "form-select mb-2"}),
        }
        labels = {
            'numero': 'Número',
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
        labels = {
            'nomevitimas': 'Nome(s) da(s) possívei(s) vítima(s)',
            'descricao_situacao':'Descrição da situação'

        }

class DireitoForm(forms.ModelForm):
    class Meta:
        model = models.Direito
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={"class": "form-control col-4"}),
        }
class AnotacaoForm(forms.ModelForm):
    class Meta:
        model = models.Anotacao
        fields = ('titulo','descricao')
        labels = {
            'titulo': 'Título',
            'descricao':'Descrição'

        }
        


    def __init__(self,*args, **kwargs):
        super(AnotacaoForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'

class VitimaForm(forms.ModelForm):
    class Meta:
        model = models.Vitima
        fields = '__all__'
        exclude = ['endereco']
        labels = {
            'nome_responsavel': 'Nome do responsável',

        }
        widgets = {
            'escola': forms.Select(attrs={"class": "form-select"})

        }

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
        self.fields['vitima'].label = "Digite o nome da(s) vítima(s) ligada(s) a essa denúncia"

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
                        self.add_error('vítima', 'Vítima já está nessa denúncia')
                    else:
                        filtro = models.Vitima.objects.filter(nome=vitima)
                        if not filtro:
                            nova_vitima = models.Vitima.objects.create(nome=vitima)
                            ocorrencia.vitimas.add(nova_vitima)
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


class CidadeForm(forms.ModelForm):
    class Meta:
        model = models.Cidade
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super(CidadeForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'   


class BairroForm(forms.ModelForm):
    class Meta:
        model = models.Bairro
        fields = '__all__'
        widgets = {
            'cidade': forms.Select(attrs={'size':'3'}),
        }
        
    def __init__(self,*args, **kwargs):
        super(BairroForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'             

class EscolaForm(forms.ModelForm):
    class Meta:
        model = models.Escola
        fields = ['nome',]
    def __init__(self,*args, **kwargs):
        super(EscolaForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'  

class StatusServidorForm(forms.Form):
    servidor = forms.ModelChoiceField(queryset=models.Servidor.objects.all())
    grupo = forms.ModelChoiceField(queryset=Group.objects.all())

    def __init__(self,*args, **kwargs):
        super(StatusServidorForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'  

class GrupoForm(forms.Form):
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'size':'3'}))

    def __init__(self,*args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-select'  

class DireitoAddForm(forms.Form):
    direito = forms.ModelChoiceField(queryset=models.Direito.objects.all())
       
    def __init__(self,*args, **kwargs):
        super(DireitoAddForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'
