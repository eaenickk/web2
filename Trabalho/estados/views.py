from django.shortcuts import render
from django.http import HttpResponse


def index(nome):
    return render(nome,"hello/index.html")

def nordeste(nome):
    return render(nome,"hello/nordeste.html")

def norte(nome):
    return render(nome,"hello/norte.html")

def ceara(nome):
    return render(nome,'hello/ceara.html')

def pernambuco(nome):
    return render(nome,'hello/pernambuco.html')