from django.shortcuts import render, redirect, get_object_or_404
from .models import Bairro, Cidade, Comunicante, Denuncia, Direito, Ocorrencia, Contato, Vitima,Anotacao, Servidor
from django.contrib import messages
import datetime
from .forms import ComunicanteForm, ContatoForm, EnderecoForm, DocumentoForm,DenunciaForm, DireitoForm, AnotacaoForm, VitimaForm, ArquivoForm, VitimaToOcorrenciaForm
from django.contrib.auth.decorators import login_required, permission_required
from dateutil.relativedelta import relativedelta
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

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
            denuncia.conselheiro = Servidor.objects.get(id=Servidor.conselheiro_para_denuncia())
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

@login_required
@permission_required('app.view_denuncia',raise_exception=True)
def lista_denuncia(request):
    if request.GET:
        if request.GET.get('filtro') == '3':
            filtro = request.GET.get('filtro')
            busca = request.GET.get('search')
            if busca:
                denuncias = Denuncia.objects
            

    else:
        denuncias = Denuncia.objects.all().filter(conselheiro=request.user.servidor)
        denuncias_geral = Denuncia.objects.all()
    
    
    contexto = {
        'titulo_pagina':'lista_denuncia',
        'denuncias':denuncias,
        'denuncias_geral':denuncias_geral
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
    
    contexto = {
        'titulo_pagina':'lista_vitima',
        'vitimas':vitimas,
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

            messages.success(request,'Vitima cadastrada')
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
            endereco = EnderecoForm(request.POST, instance=vitima.enderecos.all()[0])
            if form.is_valid() and endereco.is_valid():
                endereco  = endereco.save()
                form = form.save(commit = False)
                vitima.endereco = endereco
                form.save()
                messages.success(request,'Vitima Alterada com sucesso')
                return redirect('app:lista_vitima')
    else:
        form = VitimaForm(instance=vitima)
        if vitima.enderecos.all():
            endereco = EnderecoForm(instance=vitima.enderecos.all()[0])
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
    anotacoes = Anotacao.objects.filter(ocorrencia=ocorrencia.id)
    tutelados = ocorrencia.vitimas.all()
    
    contexto = {
        'titulo_pagina':'ocorrencia',
        'ocorrencia':ocorrencia,
        'anotacoes':anotacoes,
        'tutelados':tutelados
    }
    return render(request,'app/ocorrencia.html',contexto)


@login_required
@permission_required('app.view_ocorrencia',raise_exception=True)
def lista_ocorrencia(request):
    if request.GET:
        if request.GET.get('filtro') == '3':
            filtro = request.GET.get('filtro')
            busca = request.GET.get('search')
            if busca:
                denuncias = Denuncia.objects
            

    else:
        ocorrencias = Denuncia.objects.all().filter(conselheiro=request.user.servidor)
        

        ocorrencias_geral = Ocorrencia.objects.all()
    
    
    contexto = {
        'titulo_pagina':'lista_ocorrencia',
        'ocorrencias':ocorrencias,
        'ocorrencias_geral':ocorrencias_geral
    }
    return render(request,'app/lista_ocorrencia.html',contexto)


def ocorrencia_to_pdf_view(request,ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia,pk=ocorrencia_id)
    anotacoes = Anotacao.objects.filter(ocorrencia=ocorrencia.id)
    tutelados = ocorrencia.vitimas.all()
    html_string = render_to_string('templates/app/ocorrencia_pdf.html', {'ocorrencia': ocorrencia,'anotacoes':anotacoes,'tutelados':tutelados})

    html = HTML(string=html_string)
    html.write_pdf(target=f'/media/ocorrencia n°{ocorrencia_id}.pdf')
    fs = FileSystemStorage('/media')
    with fs.open(f'ocorrencia n°{ocorrencia_id}.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="ocorrencia n°{ocorrencia_id}"'
        return response

    return response