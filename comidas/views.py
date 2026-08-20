from django.shortcuts import render
from .models import Plato, Receta, MenuEspecial, Servicio

def inicio(request):
    return render(request, 'comidas/index.html', {
        'platos': Plato.objects.all(),  # pylint: disable=no-member
        'menus_especiales': MenuEspecial.objects.all(),  # pylint: disable=no-member
        'servicios': Servicio.objects.all() # pylint: disable=no-member
    })

def lista_recetas(request):
    return render(request, 'comidas/recetas.html', {'recetas': Receta.objects.all()})  # pylint: disable=no-member