from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserCreationForm, UserEditForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required

def registro(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        contexto = {
            'form':form
        }   
        if form.is_valid():
            profile = form.save(commit=False)
            password = form.cleaned_data['password']
            profile.set_password(password)
            form.save()
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('app:secretaria')

    else:
        form = UserCreationForm()
    contexto = {
        'form':form
    }   

    return render(request, 'accounts/registro_servidor.html', contexto)

@login_required
def update(request):
    user = request.user.servidor
    if request.method == 'POST':
        form = UserEditForm(request.POST,instance=user)
        contexto = {
            'form':form
        }   
        if form.is_valid():
            profile = form.save(commit=False)
            password = form.cleaned_data['password']
            profile.set_password(password)
            form.save()
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            login(request,profile)
            return redirect('app:secretaria')

    else:
        form = UserEditForm(instance=user)
    contexto = {
        'form':form
    }   
    return render(request, 'accounts/update.html', contexto)