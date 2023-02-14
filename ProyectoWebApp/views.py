from django.shortcuts import render, HttpResponse
from carro.carro import Carro
from servicios.models import Servicio

# Create your views here.

def inicio(request):

    carro=Carro(request)

    return render(request, "ProyectoWebApp/inicio.html")



