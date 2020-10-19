from django.shortcuts import render
from .forms import ComunicanteForm

def secretaria(request):
    contexto = {
       
    }
    
    return render(request,'app/secretaria.html',contexto)

def registro_comunicante(request):
    form = ComunicanteForm()
    if request.method == "POST":
        form = ComunicanteForm(request.POST)
        if form.is_valid():
            comunicante = form.save()
    contexto = {
        
       'form':form,
    }
    
    return render(request,'app/registro-comunicante.html',contexto)