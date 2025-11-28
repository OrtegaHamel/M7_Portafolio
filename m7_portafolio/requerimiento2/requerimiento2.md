# Requerimiento 2

**Implementar la capa de modelo de acceso a datos utilizando entidades
no relacionadas**

Este requerimiento consiste en crear modelos simples en Django **sin
relaciones entre ellos**, permitiendo que cada entidad genere una tabla
independiente en la base de datos.

El ejemplo implementado para este requerimiento es el modelo
**Producto**, el cual contiene campos básicos y no se relaciona con
ninguna otra entidad del proyecto.

## Modelo implementado

``` python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
```

## Descripción del modelo

-   **nombre**: nombre del producto (texto).\
-   **precio**: precio del producto utilizando `DecimalField`.\
-   **cantidad**: número de unidades disponibles utilizando un entero
    positivo.\
-   La clase no posee relaciones (`ForeignKey`, `ManyToMany`, etc.),
    cumpliendo el requerimiento de entidades independientes.

## Propósito del requerimiento

La finalidad es demostrar la implementación de la capa de acceso a datos
utilizando modelos aislados que resuelven una problemática simple sin
necesidad de relaciones entre entidades.
