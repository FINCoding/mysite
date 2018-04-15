# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

@csrf_protect
def login(request):
    args = {}

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            args = {'username': username}
            # return render(request, 'main.html', args)
            return redirect('/main/')
        else:
            # args('login_error')
            login_error = 'login_error'
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)

@csrf_protect
def logout(request):
    auth.logout(request)
    # print(username)
    return redirect("/main/")

@csrf_protect
def register(request):
    args = {}
    args['form'] = CustomUserCreationForm(request.POST)
    if request.POST:
        newuser_form = CustomUserCreationForm(request.POST)
        if newuser_form.is_valid():
           newuser_form.save()
           newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                       password=newuser_form.cleaned_data['password2'],
                                       email=newuser_form.cleaned_data['email'])
           auth.login(request,newuser)
           context = {'reg': 'Ура!!! Вы зарегистрированы!!! Просим войти.'}
           # return redirect("/main/")
           return render(request, 'main.html', context)
        else:
            args['form'] = newuser_form
    return render(request,'register.html', args )