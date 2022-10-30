from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

def logar(request):
    if request.method == 'POST':
        user = request.POST.get('email')
        password = request.POST.get('senha')
        
        check = auth.authenticate(request, username=user, password=password)
        
        if check is not None:
            auth.login(request, check)
            return redirect('Home')
        else:
            messages.error(request,'Dados incorretos!!!')
            return redirect('logar')    
    else:
        return render(request, 'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('logar')


def cadastro(request):
    if request.method == 'POST':
        user = request.POST.get('email')
        password = request.POST.get('senha')
        password_confirm = request.POST.get('senha_verificacao')
        
        if len(user) == 0:
            messages.error(request,'Usuário deve ser maior que 0')
            return redirect('cadastro') 
        # if len(user) == "":
        #     messages.error(request,'Não é permitido espaços em branco')
        #     return redirect('cadastro')
        
        if len(password) < 5 or len(password) > 12:
            messages.error(request,'Senha deve conter mais que 5 e menos que 12')
            return redirect('cadastro') 
        
        elif password != password_confirm:
            messages.error(request,'As senhas devem serem iguais')
            return redirect('cadastro') 
        
        if len(user) == 0 or len(password) < 5 or len(password) > 12:
            messages.error(request,'Senha deve conter mais que 5 e menos que 12')
            return redirect('cadastro') 
        else:
            User.objects.create_user(username=user, password=password)
            return redirect('logar')
             
    else:
        return render(request, 'cadastro.html')