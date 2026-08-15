from django.shortcuts import render
from .models import Plato

# Create your views here.
def inicio(_request):
    """Display the welcome page for Ana's recipes."""
    platos = Plato._default_manager.all()
    return render(_request, 'comidas/index.html', {'platos': platos})