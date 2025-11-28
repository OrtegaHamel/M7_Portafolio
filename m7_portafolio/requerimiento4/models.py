from django.db import models

class ProductoDemo(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # NUEVO CAMPO

