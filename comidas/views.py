from django.shortcuts import render
from .models import Plato, Receta, Combo

# Create your views here.
def inicio(_request):
    """Display the welcome page for Ana's recipes."""
    platos = Plato._default_manager.all()
    combos = Combo._default_manager.all()
    return render(_request, 'comidas/index.html', {'platos': platos, 'combos': combos})

def lista_recetas(_request):
    """Display the list of recipes."""
    recetas = Receta._default_manager.all()
    return render(_request, 'comidas/recetas.html', {'recetas': recetas})