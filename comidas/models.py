from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='platos/', blank=True, null=True)
    
    # Opciones de salud y estilo
    condicion_salud = models.CharField(max_length=50, blank=True, null=True)
    estilo_vida = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Receta(models.Model):
    nombre = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='recetas/', blank=True, null=True)
    ingredientes = models.TextField(help_text="Lista de ingredientes separados por líneas")
    preparacion = models.TextField(help_text="Pasos de preparación")

    def __str__(self):
        return str(self.nombre)

class Combo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(help_text="Ej: Combo familiar que incluye 3 viandas a elección")
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad_platos = models.IntegerField(default=2, help_text="Número de comidas que incluye el combo")
    imagen = models.ImageField(upload_to='combos/', blank=True, null=True)

    def __str__(self):
        return str(self.nombre)