# Requerimiento 4: Uso de Migraciones en Django

## 📌 Descripción del Requerimiento  
Este requerimiento consiste en **utilizar el sistema de migraciones de Django** para propagar cambios en el esquema de la base de datos cuando se modifican los modelos.  
Las migraciones permiten mantener la base de datos sincronizada con los modelos del proyecto sin necesidad de manipular SQL manualmente.

## 🎯 Objetivo  
Asegurar que cualquier cambio realizado en los modelos (creación de tablas, modificación de campos, eliminación, etc.) sea correctamente aplicado a la base de datos mediante migraciones.

---

## 🛠️ Desarrollo del Ejemplo  

Para este requerimiento se creó un modelo inicial llamado `ProductoDemo` y luego se agregó un nuevo campo `precio`.  
Este cambio se propagó a la base de datos mediante una migración.

### ✔️ Modelo Original
```python
from django.db import models

class ProductoDemo(models.Model):
    nombre = models.CharField(max_length=100)
```

### ✔️ Cambio realizado en el modelo  
Se agrega un nuevo campo:
```python
precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
```

### ✔️ Resultado final del modelo
```python
from django.db import models

class ProductoDemo(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
```

---

## 📄 Migración generada automáticamente por Django  
Archivo: `0002_productodemo_precio.py` (ejemplo)

```python
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('requerimiento4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productodemo',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
```

---

## 🚀 Comandos utilizados  
Para generar y aplicar la migración, se ejecutaron los comandos estándar de Django:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📸 Capturas de Pantalla  
Puedes incluir aquí capturas como:

- Generación de migraciones en consola  
- Migración aplicada exitosamente  
- Modelo modificado en el admin o shell  

**Ubicación sugerida:**  
`requerimiento4/capturas/`

---

## ✅ Conclusión  
Este requerimiento demuestra el uso correcto del sistema de migraciones de Django para mantener la base de datos alineada con los cambios realizados en los modelos.  
Es una funcionalidad esencial para cualquier proyecto Django profesional.

