from django.shortcuts import render
from .models import Articulos
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def lista_art(request):
    articulos = Articulos.objects.all().order_by('fecha_creacion')

    return render(request,'articulos/articulos.html',{'articulos': articulos})

def detalles_art(request, slug):

    articulos = Articulos.objects.get(slug=slug)

    return render(request,'articulos/detalle_articulo.html',{'articulos':articulos})

@login_required(login_url="/cuentas/login/")
def crear_art (request):
    return render(request, 'articulos/crear_articulo.html')