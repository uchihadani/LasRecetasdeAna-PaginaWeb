from django.contrib import admin
from .models import Combo, Plato, Receta

# Register your models here.
admin.site.register(Plato)
admin.site.register(Receta)
admin.site.register(Combo)