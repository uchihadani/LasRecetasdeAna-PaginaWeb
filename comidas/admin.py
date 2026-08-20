from django.contrib import admin
from .models import Plato, Receta, MenuEspecial, Servicio
from django.contrib.auth.models import Group, User

# Ocultar Grupos y Usuarios del panel principal
admin.site.unregister(Group)
admin.site.unregister(User)

# Cambiamos los nombres de los encabezados para que sean amigables
admin.site.site_header = "Panel de Control - Las Recetas de Ana"
admin.site.site_title = "Administración"
admin.site.index_title = "Bienvenida, Ana. ¿Qué quieres editar hoy?"

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    # Usamos fieldsets para agrupar los datos y que no sea una lista larga
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'imagen')
        }),
        ('Precios (El total se suma solo)', {
            'fields': ('precio', 'precio_envio')
        }),
        ('Categorías (Elige las etiquetas aquí)', {
            'fields': ('condicion_salud', 'tipo_plato', 'estilo_vida')
        }),
    )
    list_display = ('nombre', 'precio', 'precio_envio', 'precio_total')

@admin.register(MenuEspecial)
class MenuEspecialAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información del Menú', {
            'fields': ('nombre', 'descripcion', 'imagen', 'cantidad_platos')
        }),
        ('Precios', {
            'fields': ('precio', 'precio_envio')
        }),
    )
    list_display = ('nombre', 'precio', 'precio_envio', 'precio_total')

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_base', 'precio_total')