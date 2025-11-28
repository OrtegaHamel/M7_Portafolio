from django.contrib import admin
from .models import Categoria, Articulo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "categoria", "precio")
    list_filter = ("categoria",)
    search_fields = ("titulo",)
