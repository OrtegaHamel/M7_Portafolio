# Requerimiento 3  
**Implementar la capa de modelo con relaciones Uno a Uno, Uno a Muchos y Muchos a Muchos**

Este requerimiento consiste en modelar entidades relacionadas utilizando los tipos de relación proporcionados por Django:  
- `OneToOneField`  
- `ForeignKey`  
- `ManyToManyField`

El objetivo es representar un sistema donde clientes, perfiles, pedidos y productos se relacionan entre sí de acuerdo con las necesidades de la aplicación.

---

## ✔️ Modelos Implementados

### 1. **Relación Uno a Uno (OneToOneField)**  
Se crea un modelo `PerfilCliente` que almacena información adicional sobre un cliente. Cada cliente tiene exactamente un perfil.

```python
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
```

---

### 2. **Relación Uno a Muchos (ForeignKey)**  
Un cliente puede tener varios pedidos, pero cada pedido pertenece solo a un cliente.

```python
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.nombre}"
```

---

### 3. **Relación Muchos a Muchos (ManyToManyField)**  
Un pedido puede incluir muchos productos, y un producto puede estar en distintos pedidos.

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

Pedido.productos = models.ManyToManyField(Producto, related_name="pedidos")
```

---

## ✔️ Conclusión  

Este requerimiento demuestra la capacidad de Django para modelar estructuras complejas mediante relaciones entre entidades.  
El uso de OneToOne, ForeignKey y ManyToMany permite representar escenarios reales como clientes, perfiles detallados, pedidos asociados y productos compartidos.

---

## 📸 Capturas de Pantalla  
_(Agrega aquí tus imágenes una vez las tengas en tu repositorio, por ejemplo:)_

```
![Relaciones en Django](./img/relaciones.png)
```

---

## 📂 Archivos involucrados  
- `models.py` dentro de tu aplicación Django correspondiente  
- Migraciones generadas automáticamente  

---

## ▶️ Recordatorio  
Después de definir los modelos, ejecutar:

```bash
python manage.py makemigrations
python manage.py migrate
```
