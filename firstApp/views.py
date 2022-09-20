from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def ruta2(request):
    return HttpResponse("<h1>Hola Mundo! Pagina 2</h1>")