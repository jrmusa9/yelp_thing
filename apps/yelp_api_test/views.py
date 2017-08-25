# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from random import randint
from fusion import *

# Create your views here.

def index(request):
    if 'id' in request.session:
        request.session['id'] = None
    return render(request, 'yelp_api_test/index.html')  

def login(request):
    pass

def register(request):
    pass

def logout(request):
    return redirect('/')  

def home(request):
    return render(request, 'yelp_api_test/home.html')  

def add_friend(request):
    return redirect('/home')  

def categories(request):    
    return render(request, 'yelp_api_test/categories.html')

def process(request):
    print request.POST
    if request.method == 'POST':
        # arr= request.POST.getlist('category')
        # filters= ','.join(arr)
        request.session['search'] = request.POST['search']
        request.session['location_input'] = request.POST['location']
        request.session['search_results'] = query_api(request.session['search'], request.session['location_input'])
    
    return redirect('/results')

def results(request):
    search_results = request.session['search_results']
    random=randint(1,20)
    search_results=search_results['businesses'][random]
    context = {
        'places': search_results
    }


    return render(request, 'yelp_api_test/home.html', context)

def goback(request):
    return redirect('/home')