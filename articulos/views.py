from django.shortcuts import render
from .models import Articulos
from django.http import HttpResponse

# Create your views here.

def lista_art(request):
    articulos = Articulos.objects.all().order_by('fecha_creacion')

    return render(request,'articulos/articulos.html',{'articulos': articulos})

def detalles_art(request, slug):

    articulos = Articulos.objects.get(slug=slug)

    return render(request,'articulos/detalle_articulo.html',{'articulos':articulos})