from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def Home(request):
    return render(request, 'Home.html',)


def SignUp(request):
    if request.method == 'GET':
        return render(request, 'SignUp.html', {
            'form': UserCreationForm  
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                print('registrando usuario')
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('logged')
            except IntegrityError:
                return render(request, 'SignUp.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya se registro anteriormente'
                })
        return render(request, 'SignUp.html', {
            'form': UserCreationForm,
            'error': 'Las contrase;as no coinciden'
        })

def Logged(request):
    return render(request, 'Logged.html')

def LogOut(request):
    logout(request)
    return redirect('home')

def Login(request):
    if request.method == 'GET':
        return render(request, 'Login.html', {
            'form' : AuthenticationForm
        })
    else:
        user  = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Login.html', {
                'form' : AuthenticationForm,
                'error': 'los datos que ingresaste son incorrectos!!!'
            })
        else:
            login(request, user)
            return redirect('logged')