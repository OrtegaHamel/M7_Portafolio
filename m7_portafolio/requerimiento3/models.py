from django.db import models

# -------------------------------
# 1. Relación Uno a Uno (OneToOne)
# -------------------------------

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class PerfilCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"


# -----------------------------------
# 2. Relación Uno a Muchos (ForeignKey)
# -----------------------------------

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.nombre}"


# -----------------------------------------
# 3. Relación Muchos a Muchos (ManyToMany)
# -----------------------------------------

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


# Muchos a muchos: un pedido puede incluir muchos productos,
# y un producto puede estar presente en muchos pedidos.
Pedido.productos = models.ManyToManyField(Producto, related_name="pedidos")

