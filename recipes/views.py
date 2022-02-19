from multiprocessing import context
from unicodedata import name

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Sergio Lucas',
    })


def recipe(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Sergio Lucas',
    })
