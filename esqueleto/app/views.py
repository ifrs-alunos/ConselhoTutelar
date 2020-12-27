from django.shortcuts import render, redirect, get_object_or_404
from .models import Bairro, Cidade, Comunicante, Denuncia, Direito, Ocorrencia, Contato, Vitima,Anotacao
from django.contrib import messages
import datetime
from .forms import ComunicanteForm, ContatoForm, EnderecoForm, DocumentoForm,DenunciaForm, DireitoForm, AnotacaoForm, VitimaForm

def secretaria(request):
    contexto = {
       
    }
    
    return render(request,'app/secretaria.html',contexto)

def registro_comunicante(request):
    if request.method == "POST":
        contato= ContatoForm(request.POST)
        endereco = EnderecoForm(request.POST)
        comunicante = ComunicanteForm(request.POST)
        documento = DocumentoForm(request.POST)
        denuncia = DenunciaForm(request.POST)
        teste = Cidade.dicionario_cidade_bairro()
        contexto = {
            'contato':contato,
            'comunicante':comunicante,
            'endereco':endereco,
            'documento':documento,
            'denuncia':denuncia,
            'teste':teste,
        }    

        if comunicante.is_valid() and contato.is_valid() and endereco.is_valid() and documento.is_valid() and denuncia.is_valid():
            endereco  = endereco.save()
            comunicante = comunicante.save(commit = False)
            comunicante.endereco = endereco
            comunicante.save()


            documento = documento.save(commit= False)
            documento.comunicante = comunicante
            documento.save()

            contato= contato.save(commit = False)
            contato.comunicante = comunicante
            contato.save()

            denuncia = denuncia.save(commit = False)
            denuncia.comunicante = comunicante
            denuncia.save()
            messages.success(request,'')
            return redirect('app:secretaria')
        else:
            return render(request,'app/registro-comunicante.html',contexto)

    else:
        comunicante = ComunicanteForm()
        contato = ContatoForm()
        endereco = EnderecoForm()
        documento = DocumentoForm()
        denuncia = DenunciaForm()
        

    teste = Cidade.dicionario_cidade_bairro()
    

    contexto = {
        'contato':contato,
        'comunicante':comunicante,
        'endereco':endereco,
        'documento':documento,
        'denuncia':denuncia,
        'teste':teste,
    }
    
    return render(request,'app/registro-comunicante.html',contexto)

def lista_denuncia(request):
    if request.GET:
        if request.GET.get('filtro') == '3':
            filtro = request.GET.get('filtro')
            busca = request.GET.get('search')
            if busca:
                denuncias = Denuncia.objects
            

    else:

        denuncias = Denuncia.objects.all()
    
    
    contexto = {
        'titulo_pagina':'lista_denuncia',
        'denuncias':denuncias,
    }
    return render(request,'app/lista_denuncia.html',contexto)


def visualizar_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia,pk=denuncia_id)
    contatos = Contato.objects.filter(comunicante=denuncia.comunicante.id)
    
    contexto = {
        'titulo_pagina':'denuncia',
        'denuncia':denuncia,
        'contatos':contatos
    }
    return render(request,'app/visualizar_denuncia.html',contexto)

def lista_vitima(request):
    busca = request.GET.get('search')
    if busca:
        vitimas = Vitima.objects.filter(nome__contains=busca)
    else:

        vitimas = Vitima.objects.all()
        print(datetime.datetime.now().year-18)
    maioridades = Vitima.objects.filter(data_nascimento__year=datetime.datetime.now().year-18)
    
    contexto = {
        'titulo_pagina':'lista_vitima',
        'vitimas':vitimas,
        'maioridades': maioridades
    }
    return render(request,'app/lista_vitima.html',contexto)

def cadastrar_vitima(request):
    if request.method == "POST":
        vitima = VitimaForm(request.POST)
        if vitima.is_valid():
            vitima.save()
            messages.success(request,'Vitima cadastrada')
            return redirect('app:secretaria')
    else:
        vitima = VitimaForm()
    
    contexto = {
        'vitima':vitima
    }
    
    return render(request,'app/cadastrar_vitima.html',contexto)

        


def visualizar_vitima(request, vitima_id):
    vitima = get_object_or_404(Vitima,pk=vitima_id)
    ocorrencias = Ocorrencia.objects.filter(vitimas=vitima.id)
    
    contexto = {
        'titulo_pagina':'vitima',
        'vitima':vitima,
        'ocorrencias':ocorrencias,
    }
    return render(request,'app/visualizar_vitima.html',contexto)


def adicionar_anotacao(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia,pk=ocorrencia_id)
    if request.method == "POST":
        form = AnotacaoForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.ocorrencia = ocorrencia    
            form.save() 
            messages.success(request,'Vitima cadastrada')
            return redirect('app:ocorrencia',ocorrencia_id= ocorrencia_id)
    else:
        form = AnotacaoForm


    contexto = {
        'form':form,
        'ocorrencia_id':ocorrencia_id
    }
    return render(request,'app/adicionar_anotacao.html',contexto)
    

def vitima_update(request, vitima_id):
    vitima = get_object_or_404(Vitima,pk=vitima_id)
    if request.method =="POST":
            form = VitimaForm(request.POST, instance=vitima)
            if form.is_valid():
                form.save()
                messages.success(request,'Vitima Alterada com sucesso')
                return redirect('app:lista_vitima')
    else:
        form = VitimaForm(instance=vitima)
        contexto = {
            "form":form,
            'vitima_id':vitima_id
        }
        return render(request, "app/vitima_update.html",contexto)
                


def ocorrencia(request,ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia,pk=ocorrencia_id)
    anotacoes = Anotacao.objects.filter(ocorrencia=ocorrencia.id)
    tutelados = ocorrencia.vitimas.all()
    contexto = {
        'titulo_pagina':'ocorrencia',
        'ocorrencia':ocorrencia,
        'anotacoes':anotacoes,
        'tutelados':tutelados
    }
    return render(request,'app/ocorrencia.html',contexto)