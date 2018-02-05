# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
# from django.template.loader import get_template
# from django.template import Context

@csrf_protect
def login(request):
    print("Hello")
    args = {}
    print(request.POST)
    if request.POST:
        print('я тут')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            context = {'username': username}
            return render(request, 'main.html', context)
        else:
            # args('login_error')
            print('я еуе')
            login_error = 'login_error'
            return render(request, 'login.html', args)
    else:
        print('или тут')
        return render(request, 'login.html', args)

@csrf_protect
def logout(request):
    auth.logout(request)
    # print(username)
    return redirect("/main/")

@csrf_protect
def register(request):
    args = {}
    #
    args['form'] = UserCreationForm(request.POST)
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
           newuser_form.save()
           newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
           auth.login(request,newuser)
           context = {'reg': 'Ура!!! Вы зарегистрированы!!! Просим войти.'}
           # return redirect("/main/")
           return render(request, 'main.html', context)
        else:
            args['form'] = newuser_form
    return render(request,'register.html', args )