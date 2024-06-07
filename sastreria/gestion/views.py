from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/clientes.html', {'clientes': clientes})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la Sastrería!")

