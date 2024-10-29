from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def calcular_huella(request):
    return render(request, 'calcular_huella.html')
