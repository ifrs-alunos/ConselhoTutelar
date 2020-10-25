from django.shortcuts import render
from .forms import ComunicanteForm, ContatoForm, EnderecoForm, DocumentoForm,DenunciaForm, DireitoForm

def secretaria(request):
    contexto = {
       
    }
    
    return render(request,'app/secretaria.html',contexto)

def registro_comunicante(request):
    comunicante = ComunicanteForm()
    contato = ContatoForm()
    endereco = EnderecoForm()
    documento = DocumentoForm()
    denuncia = DenunciaForm()
    direito = DireitoForm()
    if request.method == "POST":
        contato= ContatoForm(request.POST)
        comunicante = ComunicanteForm(request.POST)
        endereco = EnderecoForm(request.POST)
        documento = DocumentoForm(request.POST)
        denuncia = DenunciaForm(request.POST)
        direito = DireitoForm(request.POST)


        if comunicante.is_valid() and contato.is_valid() and endereco.is_valid() and documento.is_valid() and denuncia.is_valid():

            endereco = endereco.save()
            
            
            comunicante = comunicante.save(commit = False)
            comunicante.enderecos = enderecos
            comunicante = comunicante.save()

            documento = documento.save(commit= False)
            documento.comunicante = comunicante
            documento.save()

            contato= contato.save(commit = False)
            contato.comunicante = comunicante
            contato.save()

            denuncia.save()
            direito = direito.save(commit = False)
            direto.denuncia = denuncia
            direito.save()


              

    contexto = {
        'contato':contato,
       'comunicante':comunicante,
       'endereco':endereco,
       'documento':documento,
       'denuncia':denuncia,
       'direito':direito
    }
    
    return render(request,'app/registro-comunicante.html',contexto)