# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..login.models import User
from models import Comment

def dashboard(request):
    context = {
        'user':User.objects.exclude(id = request.session['id']),
    }
    if 'first_name' not in request.session:
        return redirect('/') #All important routes that users shouldn't be able to access without being logged in should have this line!!!!!

    return render(request, "reviews/books.html", context)

def showUser(request, id):
    context = {
        'user': User.objects.get(id = id)
    }
    if 'first_name' not in request.session:
        return redirect('/')

    return render(request, "reviews/user.html", context)

def addComment(request):
    results = Comment.objects.commentVal(request.POST)
    if len(results['errors']) > 0:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/user/' + request.POST['user_id'])

    Comment.objects.create(
        contents = request.POST['comment'], 
        poster = User.objects.get(id = request.POST['poster_id']), 
        user = User.objects.get(id = request.POST['user_id']))
    messages.success(request, 'Comment posted successfully.')
    return redirect('/user/' + request.POST['user_id'])

def books(request):
    if 'first_name' not in request.session:
        return redirect('/')

    return render(request, "reviews/add.html")