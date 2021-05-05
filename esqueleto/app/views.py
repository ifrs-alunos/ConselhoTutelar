from django.shortcuts import render, redirect, get_object_or_404
from .models import Bairro, Cidade, Comunicante, Denuncia, Direito, Ocorrencia, Contato, Vitima,Anotacao, Servidor, Log, Escola
from django.contrib import messages
import datetime
from .forms import ComunicanteForm, ContatoForm, EnderecoForm, DocumentoForm,DenunciaForm, DireitoForm, AnotacaoForm, VitimaForm, ArquivoForm, VitimaToOcorrenciaForm, CidadeForm,BairroForm,EscolaForm, StatusServidorForm, GrupoForm,DireitoAddForm, ContatoFormSet
from django.contrib.auth.decorators import login_required, permission_required
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator

from .utils import render_to_pdf 

from django import template
import base64
import requests

@login_required
def secretaria(request):
    contexto = {
       
    }
    
    return render(request,'app/secretaria.html',contexto)

@login_required
@permission_required('app.add_comunicante',raise_exception=True)
def registro_comunicante(request):
    if request.method == "POST":
        contato= ContatoForm(request.POST)
        endereco = EnderecoForm(request.POST)
        comunicante = ComunicanteForm(request.POST)
        documento = DocumentoForm(request.POST)
        denuncia = DenunciaForm(request.POST)
        formset = ContatoFormSet(request.POST)
        print(formset)
        teste = Cidade.dicionario_cidade_bairro()
        contexto = {
            'contato':contato,
            'comunicante':comunicante,
            'endereco':endereco,
            'documento':documento,
            'denuncia':denuncia,
            'teste':teste,
        }    

        if comunicante.is_valid() and contato.is_valid() and endereco.is_valid() and documento.is_valid() and denuncia.is_valid() and formset.is_valid():
            if not request.POST['nome']:
                comunicante = Comunicante.objects.get(nome='ANONIMO')
            else:
                endereco  = endereco.save()
                comunicante = comunicante.save(commit = False)
                comunicante.endereco = endereco
                comunicante.save()

            documento = documento.save(commit= False)
            documento.comunicante = comunicante
            documento.save()
            for form in formset:
                form = form.save(commit=False)
                form.comunicante = comunicante
                form.save()
            denuncia = denuncia.save(commit = False)
            denuncia.comunicante = comunicante
            denuncia.conselheiro = Servidor.objects.get(id=Servidor.conselheiro_para_denuncia())
            denuncia.save()
            messages.success(request,'Registro de Denuncia foi feito com sucesso')
            return redirect('app:secretaria')
        else:
            return render(request,'app/registro-comunicante.html',contexto)

    else:
        comunicante = ComunicanteForm()
        contato = ContatoForm()
        endereco = EnderecoForm()
        documento = DocumentoForm()
        denuncia = DenunciaForm()
        formset = ContatoFormSet()
        
    
    teste = Cidade.dicionario_cidade_bairro()
    

    contexto = {
        'contato':contato,
        'comunicante':comunicante,
        'endereco':endereco,
        'documento':documento,
        'denuncia':denuncia,
        'teste':teste,
        'formset':formset
    }
    
    return render(request,'app/registro-comunicante.html',contexto)

@login_required
@permission_required('app.view_denuncia',raise_exception=True)
def lista_denuncia(request):
    if request.GET:
        busca = request.GET.get('search')
        if busca and busca != '':
            denuncias = Denuncia.objects.filter(conselheiro=request.user.servidor).filter(comunicante__nome__contains=busca)
            denuncias_geral = Denuncia.objects.all().filter(comunicante__nome__contains=busca)
        else:    
            denuncias = Denuncia.objects.all().filter(conselheiro=request.user.servidor)
            denuncias_geral = Denuncia.objects.all()

    else:
        denuncias = Denuncia.objects.all().filter(conselheiro=request.user.servidor)
        denuncias_geral = Denuncia.objects.all()
    
    paginator_denuncia = Paginator(denuncias.order_by('-horario'), 12)
    page_number = request.GET.get('page')
    page_obj = paginator_denuncia.get_page(page_number)

    paginator_geral = Paginator(denuncias_geral.order_by('-horario'), 12)
    page_number_geral = request.GET.get('page_geral')
    page_obj_geral = paginator_geral.get_page(page_number_geral)
    contexto = {
        'titulo_pagina':'lista_denuncia',
        'denuncias':page_obj,
        'denuncias_geral':page_obj_geral
    }
    return render(request,'app/lista_denuncia.html',contexto)

@login_required
@permission_required('app.view_denuncia',raise_exception=True)
def visualizar_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia,pk=denuncia_id)
    contatos = Contato.objects.filter(comunicante=denuncia.comunicante.id)
    if Ocorrencia.objects.all().filter(denuncia=denuncia):
        vitimas_ja_ligadas = Ocorrencia.objects.get(denuncia=denuncia).vitimas.all()
    else: 
        vitimas_ja_ligadas = ''
    vitimas = Vitima.objects.all()
    if request.method == "POST":
        form = VitimaToOcorrenciaForm(request.POST,denuncia=denuncia_id)
        if form.is_valid():
            return redirect('app:visualizar_denuncia',denuncia_id)
    else:
        form = VitimaToOcorrenciaForm(denuncia=denuncia_id)
    contexto = {
        'titulo_pagina':'denuncia',
        'denuncia':denuncia,
        'contatos':contatos,
        'form':form,
        'vitimas':vitimas,
        'vitimas_ja_ligadas':vitimas_ja_ligadas
    }
    return render(request,'app/visualizar_denuncia.html',contexto)

@login_required
@permission_required('app.view_vitima',raise_exception=True)
def lista_vitima(request):
    busca = request.GET.get('search')
    if busca:
        vitimas = Vitima.objects.filter(nome__contains=busca)
    else:
        vitimas = Vitima.objects.all()
    data_inicio = datetime.datetime.now()+relativedelta(years=-18)+relativedelta(months=-1)
    data_fim =  datetime.datetime.now()+relativedelta(years=-18)+relativedelta(months=+1)
    maioridades =  Vitima.objects.filter(data_nascimento__range=(data_inicio,data_fim))

    paginator_vitima = Paginator(vitimas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator_vitima.get_page(page_number)
    contexto = {
        'titulo_pagina':'lista_vitima',
        'vitimas':page_obj,
        'maioridades': maioridades
    }
    return render(request,'app/lista_vitima.html',contexto)

@login_required
@permission_required('app.add_vitima',raise_exception=True)
def cadastrar_vitima(request):
    if request.method == "POST":
        vitima = VitimaForm(request.POST)
        endereco = EnderecoForm(request.POST)
        if vitima.is_valid() and endereco.is_valid():
            endereco  = endereco.save()
            vitima = vitima.save(commit = False)
            vitima.endereco = endereco
            vitima.save()
            messages.success(request,'Vitima cadastrada')
            return redirect('app:secretaria')
    else:
        vitima = VitimaForm()
        endereco = EnderecoForm()

    contexto = {
        'vitima':vitima,
        'endereco':endereco
    }
    
    return render(request,'app/cadastrar_vitima.html',contexto)

        

@login_required
@permission_required('app.view_vitima',raise_exception=True)
def visualizar_vitima(request, vitima_id):
    vitima = get_object_or_404(Vitima,pk=vitima_id)
    ocorrencias = Ocorrencia.objects.filter(vitimas=vitima.id)
    
    contexto = {
        'titulo_pagina':'vitima',
        'vitima':vitima,
        'ocorrencias':ocorrencias,
    }
    return render(request,'app/visualizar_vitima.html',contexto)

@login_required
@permission_required('app.add_anotacao',raise_exception=True)
def adicionar_anotacao(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia,pk=ocorrencia_id)
    if request.method == "POST":
        form = AnotacaoForm(request.POST)
        arquivoform = ArquivoForm(request.POST)
        arquivos = request.FILES.getlist('upload')
        if form.is_valid() and arquivoform.is_valid():
            form = form.save(commit=False)
            form.ocorrencia = ocorrencia    
            form.save() 
            for arquivo in arquivos:
                arquivoform = ArquivoForm(request.POST)
                arquivoform = arquivoform.save(commit=False)
                form_nome = form.titulo
                arquivoform.titulo = f'{form_nome}-{arquivo.name}'
                arquivoform.upload = arquivo
                arquivoform.ocorrencia = ocorrencia
                arquivoform.anotacao = form
                arquivoform.save()

            messages.success(request,'Anotação cadastrada')
            return redirect('app:ocorrencia',ocorrencia_id= ocorrencia_id)
    else:
        form = AnotacaoForm
        arquivoform = ArquivoForm()


    contexto = {
        'form':form,
        'arquivo':arquivoform,
        'ocorrencia_id':ocorrencia_id
    }
    return render(request,'app/adicionar_anotacao.html',contexto)
    
@login_required
@permission_required('app.change_vitima',raise_exception=True)
def vitima_update(request, vitima_id):
    vitima = get_object_or_404(Vitima,pk=vitima_id)
    if request.method =="POST":
            form = VitimaForm(request.POST, instance=vitima)
            endereco = EnderecoForm(request.POST, instance=vitima.endereco)    
            if form.is_valid() and endereco.is_valid():
                endereco  = endereco.save()
                form = form.save(commit = False)
                vitima.endereco = endereco
                
                form.save()
                messages.success(request,'Vitima Alterada com sucesso')
                return redirect('app:lista_vitima')
    else:
        form = VitimaForm(instance=vitima)
        if vitima.endereco:
            endereco = EnderecoForm(instance=vitima.endereco)
        else:
            endereco = EnderecoForm()
        contexto = {
            "form":form,
            'vitima_id':vitima_id,
            "endereco":endereco
        }
        return render(request, "app/vitima_update.html",contexto)
                

@login_required
@permission_required('app.view_ocorrencia',raise_exception=True)
def ocorrencia(request,ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia,pk=ocorrencia_id)
    
    anotacoes = Anotacao.objects.filter(ocorrencia=ocorrencia.id).order_by('-data')
    paginator_ano = Paginator(anotacoes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator_ano.get_page(page_number)
    tutelados = ocorrencia.vitimas.all()
    
    contexto = {
        'titulo_pagina':'ocorrencia',
        'ocorrencia':ocorrencia,
        'anotacoes':page_obj,
        'tutelados':tutelados
    }
    return render(request,'app/ocorrencia.html',contexto)


@login_required
@permission_required('app.view_ocorrencia',raise_exception=True)
def lista_ocorrencia(request):
    if request.GET:
        busca = request.GET.get('search')            
        if busca and busca !='':
            ocorrencias = Ocorrencia.objects.all().filter(denuncia__conselheiro=request.user.servidor).filter(denuncia__conselheiro__first_name__contains=busca)
            ocorrencias_geral = Ocorrencia.objects.all().filter(denuncia__conselheiro__first_name__contains=busca)
        else:
            ocorrencias = Ocorrencia.objects.all().filter(denuncia__conselheiro=request.user.servidor)
            ocorrencias_geral = Ocorrencia.objects.all()

    else:
        ocorrencias = Ocorrencia.objects.all().filter(denuncia__conselheiro=request.user.servidor)
        ocorrencias_geral = Ocorrencia.objects.all()
    
    paginator_ocorrencia = Paginator(ocorrencias.order_by('-denuncia__horario'), 12)
    page_number = request.GET.get('page')
    page_obj = paginator_ocorrencia.get_page(page_number)

    paginator_geral = Paginator(ocorrencias_geral.order_by('-denuncia__horario'), 12)
    page_number_geral = request.GET.get('page_geral')
    page_obj_geral = paginator_geral.get_page(page_number_geral)
    contexto = {
        'titulo_pagina':'lista_ocorrencia',
        'ocorrencias':page_obj,
        'ocorrencias_geral':page_obj_geral
    }
    return render(request,'app/lista_ocorrencia.html',contexto)

@login_required
def gerar_pdf_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia,pk=ocorrencia_id)
    anotacoes = Anotacao.objects.filter(ocorrencia=ocorrencia.id)
    tutelados = ocorrencia.vitimas.all()
    images = ocorrencia.arquivo_set.all()
    data = {
        'ocorrencia':ocorrencia,
        'anotacoes':anotacoes,
        'tutelados':tutelados,
        'images':images,
    }
    pdf = render_to_pdf('pdf/ocorrencia_pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required
def gerar_pdf_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia,pk=denuncia_id)
    if Ocorrencia.objects.all().filter(denuncia=denuncia):
        vitimas_ja_ligadas = Ocorrencia.objects.get(denuncia=denuncia).vitimas.all()
    else: 
        vitimas_ja_ligadas = ''
    data = {
    'denuncia':denuncia,
    'vitimas_ja_ligadas':vitimas_ja_ligadas
    }
    pdf = render_to_pdf('pdf/denuncia_pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required
def gerar_pdf_vitima(request, vitima_id):
    vitima = get_object_or_404(Vitima,pk=vitima_id)
    ocorrencias = Ocorrencia.objects.filter(vitimas=vitima.id)
    data = {
    'vitima':vitima,
    'ocorrencias':ocorrencias
    
    }
    pdf = render_to_pdf('pdf/vitima_pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required
@permission_required('app.view_cidade',raise_exception=True)
def dados_gerais(request,acao):
    if acao =='geral':
        queryset=''
        objeto = ''
    elif acao == 'cidade':
        queryset= Cidade.objects.all()
        objeto = 'cidade'
    elif acao =='bairro':
        queryset=Bairro.objects.all()
        objeto = 'bairro'

    elif acao =='direito':
        queryset=Direito.objects.all()
        objeto = 'direito'

    elif acao =='escola':
        queryset= Escola.objects.all()
        objeto = 'escola'
    elif acao =='servidor':
        if request.user.groups.filter(name='Coordenadores').exists():
            queryset=Servidor.objects.all()
            objeto = 'servidor'
        else:
            return redirect('app:dados_gerais','geral')
    else:
        return redirect('app:dados_gerais','geral')
    contexto = {
        'titulo_pagina':'Dados Gerais',
        'queryset':queryset,
        'acao':acao,
        'objeto':objeto
    }
    return render(request,'app/dados_gerais.html',contexto)


@login_required
@permission_required('app.change_cidade',raise_exception=True)
def dado_update(request,objeto,objeto_id):
    if request.method == 'POST':
            if objeto == 'cidade':
                cidade = get_object_or_404(Cidade,pk=objeto_id)
                form = CidadeForm(request.POST,instance=cidade)
                if form.is_valid():
                    form.save()
                    return redirect('app:dados_gerais','geral')
            
            elif objeto =='bairro':
                bairro = get_object_or_404(Bairro,pk=objeto_id)
                form = BairroForm(request.POST, instance=bairro)
                if form.is_valid():
                    form.save()
                    return redirect('app:dados_gerais','geral')

            elif objeto =='direito':
                direito = get_object_or_404(Direito,pk=objeto_id)
                form = DireitoForm(request.POST, instance=direito)
                if form.is_valid():
                    form.save()
                    return redirect('app:dados_gerais','geral')
            elif objeto =='escola':
                escola = get_object_or_404(Escola,pk=objeto_id)
                form = EscolaForm(request.POST,instance=escola)
                endereco = EnderecoForm(request.POST,instance=escola.endereco)
                if form.is_valid() and endereco.is_valid():
                        endereco.save()
                        form.save(commit=False)
                        form.endereco = endereco
                        form.save()
                        return redirect('app:dados_gerais','geral')
            elif objeto =='servidor':
                servidor = get_object_or_404(Servidor,pk=objeto_id)
                form = GrupoForm(request.POST)
                if form.is_valid():
                    grupo = form.cleaned_data.get('grupo')
                    servidor.groups.clear()
                    grupo.user_set.add(servidor)
                    return redirect('app:dados_gerais','geral')

            else:
                return redirect('app:dados_gerais','geral')
    else:
        if objeto == 'cidade':
            cidade = get_object_or_404(Cidade,pk=objeto_id)
            form = CidadeForm(instance=cidade)
        elif objeto =='bairro':
            bairro = get_object_or_404(Bairro,pk=objeto_id)
            form = BairroForm(instance=bairro)

        elif objeto =='direito':
            direito = get_object_or_404(Direito,pk=objeto_id)
            form = DireitoForm(instance=direito)
        elif objeto =='escola':
            escola = get_object_or_404(Escola,pk=objeto_id)
            form = EscolaForm(instance=escola)
            endereco = EnderecoForm(instance=escola.endereco)
            
        elif objeto =='servidor':
            if request.user.groups.filter(name='Coordenadores').exists():
                servidor = get_object_or_404(Servidor,pk=objeto_id)
                form = GrupoForm()
            else:
                return redirect('app:dados_gerais','geral')
        else:
            return redirect('app:dados_gerais','geral')
    if objeto=='escola':    
        contexto = {
            'titulo_pagina':'Atualizar dado',
            'form':form,
            'endereco':endereco,
            'objeto':objeto
        }
    elif objeto=='servidor':    
        contexto = {
            'titulo_pagina':'Atualizar dado',
            'form':form,
            'objeto':objeto,
            'servidor':servidor
        }
    else:
        contexto = {
            'titulo_pagina':'Atualizar dado',
            'form':form,
            'objeto':objeto
        }
    return render(request,'app/dado_update.html',contexto)

@login_required
@permission_required('app.add_cidade',raise_exception=True)
def dado_add(request,objeto):
    if request.method == 'POST':
            if objeto == 'cidade':
                form = CidadeForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('app:dados_gerais','geral')
            
            elif objeto =='bairro':
                form = BairroForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('app:dados_gerais','geral')

            elif objeto =='direito':
                form = DireitoForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('app:dados_gerais','geral')
            elif objeto =='escola':
                form = EscolaForm(request.POST)
                endereco = EnderecoForm(request.POST)
                if form.is_valid() and endereco.is_valid():
                        endereco.save()
                        form.save(commit=False)
                        form.endereco = endereco
                        form.save()
                        return redirect('app:dados_gerais','geral')
        
            else:
                return redirect('app:dados_gerais','geral')
    else:
        if objeto == 'cidade':
            form = CidadeForm()
        elif objeto =='bairro':
            form = BairroForm()

        elif objeto =='direito':
            form = DireitoForm()
        elif objeto =='escola':
            form = EscolaForm()
            endereco = EnderecoForm()
        else:
            return redirect('app:dados_gerais','geral')
    if objeto=='escola':    
        contexto = {
            'titulo_pagina':'Atualizar dado',
            'form':form,
            'endereco':endereco,
            'objeto':objeto
        }
    else:
        contexto = {
            'titulo_pagina':'Atualizar dado',
            'form':form,
            'objeto':objeto
        }
    return render(request,'app/dado_add.html',contexto)


@login_required
def logs_geral(request):
   
    logs = Log.objects.all().order_by('-data')
    paginator_logs = Paginator(logs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator_logs.get_page(page_number)

    contexto = {
        'titulo_pagina':'lista_logs',
        'logs':page_obj,
    }
    return render(request,'app/logs_geral.html',contexto)

@login_required
@permission_required('app.add_direito',raise_exception=True)
def add_direito(request,denuncia_id):
    denuncia = get_object_or_404(Denuncia,pk=denuncia_id)
    if request.method == "POST":
        direito = DireitoAddForm(request.POST)
        if direito.is_valid():
            direito = direito.cleaned_data.get('direito')
            denuncia.direito_set.add(direito)
            messages.success(request,'direito adicionado')
            return redirect('app:visualizar_denuncia',denuncia_id)
    else:
        direito = DireitoAddForm()

    contexto = {
        'direito':direito,
    }
    
    return render(request,'app/add_direito.html',contexto)



