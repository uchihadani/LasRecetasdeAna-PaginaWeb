from django.db import models

class Plato(models.Model):
    SALUD_CHOICES = [('diabetes', 'Diabetes'), ('hipertension', 'Hipertensión'), ('higado_graso', 'Hígado graso'), ('colon_irritable', 'Colon irritable'), ('proteica', 'Proteica'), ('otras', 'Otras')]
    TIPO_CHOICES = [('pollo', 'Pollo'), ('pescado', 'Pescado'), ('veggies', 'Veggies'), ('carne_roja', 'Carnes rojas')]
    ESTILO_CHOICES = [('vegano', 'Vegano'), ('vegetariano', 'Vegetariano'), ('keto', 'Keto')]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    precio_envio = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    imagen = models.ImageField(upload_to='platos/', blank=True, null=True)
    
    condicion_salud = models.CharField(max_length=50, choices=SALUD_CHOICES, blank=True, null=True)
    tipo_plato = models.CharField(max_length=50, choices=TIPO_CHOICES, blank=True, null=True)
    estilo_vida = models.CharField(max_length=50, choices=ESTILO_CHOICES, blank=True, null=True)

    @property
    def precio_total(self):
        return (self.precio or 0) + (self.precio_envio or 0)

    def __str__(self):
        return str(self.nombre)

class MenuEspecial(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    precio_envio = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    cantidad_platos = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to='menus/', blank=True, null=True)

    @property
    def precio_total(self):
        return (self.precio or 0) + (self.precio_envio or 0)

    def __str__(self):
        return str(self.nombre)

class Receta(models.Model):
    nombre = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='recetas/', blank=True, null=True)
    ingredientes = models.TextField()
    preparacion = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ej: Viandas Empresariales o Viandas Infantiles")
    descripcion = models.TextField(help_text="Descripción del servicio para el cliente")
    imagen = models.ImageField(upload_to='servicios/', blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=0, default=0, help_text="Precio base o desde cuánto")
    precio_envio = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    @property
    def precio_total(self):
        return (self.precio_base or 0) + (self.precio_envio or 0)

    def __str__(self):
        return str(self.nombre)