# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):

    return render(request, "login/index.html")

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        User.objects.createUser(request.POST)
        messages.success(request, "Account has been successfully created.")
    else:
        for error in results['errors']:
            messages.error(request, error)

    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['first_name'] = results['user'].first_name
        request.session['id'] = results['user'].id
        request.session['email'] = results['user'].email
        return redirect('/books')