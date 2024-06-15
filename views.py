from django.shortcuts import render,redirect
from django.contrib.auth import login as lg
from .custom_authentification import CustomAuthentification
from django.contrib import messages
from .models import MyUser
from datetime import datetime
# Create your views here.

"""Definissons la vue signup qui permet de l'utlisateur de creer son compte :
      - L'email et numero de telephone de l'utilisateur doivent etre unique """
def signup(request):
    if request.method == 'POST':
        if MyUser.objects.filter(email=request.POST['email']).exists():
            message=messages.error(request, 'Error 1 : A client with this email already exists')
        if MyUser.objects.filter(phone=request.POST['phone']).exists():
            message=messages.error(request, 'Error 2 : A client with this phone number already exists')
        return render(request, 'signup.html', {'message': message})
        user=MyUser(
            firstname=request.POST['firstname'],
            lastname=request.POST['secondname'],
            email=request.POST['email'],
            password=request.POST['pwd1'],
            phone=request.POST['phone'],
            birthday=datetime.strptime(request.POST['birthday'], "%Y-%m-%d").date()
            )
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

"""Definissons la vue login qui permet de s'authentifier l'utilisateur'"""
def login(request):
    if request.method == 'POST':
        auth=CustomAuthentification()
        user=auth.authenticate(request,request.POST['email'], request.POST['password'])
        if user is not None:
            user.last_login = datetime.now()
            user.save()
            lg(request,user,backend='Authentification.custom_authentification.CustomAuthentification')
            return redirect('home')
        else:
            redirect('login')
    return render(request,'login.html')

