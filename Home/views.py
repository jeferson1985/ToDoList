from pickle import FALSE
from django.shortcuts import render, redirect
from .models import Tasks
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required(redirect_field_name='logar')
def index(request):
    
    if request.user.is_superuser:
        tasks = Tasks.objects.all()
        return render(request, 'index.html', {'tasks':tasks})
    else:
        tasks = Tasks.objects.all()
        return render(request, 'index.html', {'tasks': tasks})
    

def addTask(request):
    return render(request, 'addTask.html')


def addItem(request):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    data = request.POST.get('data')
    status = request.POST.get('status')
    
    
    if status == 'Pendente':
        status = False
    else:
        status = True 
          
    Tasks.objects.create(title=titulo, descriptions=descricao, date=data, status=status, usuario_id=request.user.id)
    return redirect('Home')


def deletar(request, id):
    Tasks.objects.get(id=id).delete()
    return redirect('Home')

def finalizar(request, id):
    item = Tasks.objects.get(id=id)
    item.status = True
    item.save()
    return redirect('Home')

def editar(request, id):
    item = Tasks.objects.get(id=id)
    if request.method == 'POST':
        item = Tasks.objects.get(id=id)
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        status = request.POST.get('status')
        
        if status == 'Pendente':
            status = False
        else:
            status = True
        
        item.title = titulo
        item.descriptions = descricao
        item.date = data
        item.status = status
        item.save()
        return redirect('Home')
    else:
        return render(request, 'editTask.html', {'item':item})
    
    

def buscar(request):
    termo = request.GET.get('termo')#name="termo" no html
    tasks = Tasks.objects.filter(title__icontains =termo)#icontains usado para filtrar
    return  render(request, 'index.html', {'tasks': tasks})