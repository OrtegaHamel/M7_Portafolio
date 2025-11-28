## 🧩 Requerimiento 7: Reconocer las aplicaciones preinstaladas de Django y su utilidad

Django incluye un conjunto de aplicaciones internas dentro del paquete `django.contrib`, las cuales proporcionan funcionalidades esenciales que facilitan el desarrollo de aplicaciones web completas. Este requerimiento busca identificar estas aplicaciones preinstaladas y demostrar su uso dentro del proyecto.

---

### 🔹 Aplicaciones preinstaladas más importantes

#### **1. django.contrib.admin**
Proporciona el **panel de administración** listo para usar, donde es posible gestionar modelos, aplicar filtros, realizar búsquedas y administrar permisos.  
Es una herramienta fundamental para revisar y manipular datos sin construir interfaces manualmente.

---

#### **2. django.contrib.auth**
Sistema completo de **autenticación y autorización**, que incluye:
- Inicio y cierre de sesión  
- Permisos y grupos  
- Administración de usuarios  

Es la base del control de acceso en Django.

---

#### **3. django.contrib.sessions**
Permite guardar información temporal del usuario entre solicitudes mediante **sesiones**.  
Es esencial para manejar autenticación, carritos de compra u otros datos temporales.

---

#### **4. django.contrib.messages**
Sistema para mostrar mensajes temporales en la interfaz:  
- Éxito  
- Error  
- Advertencias  
- Información  

Es comúnmente usado en formularios y procesos CRUD.

---

#### **5. django.contrib.staticfiles**
Gestiona archivos estáticos del proyecto como **CSS, JavaScript e imágenes**, permitiendo organizarlos y servirlos correctamente tanto en desarrollo como en producción.

---

### 🛠️ Configuración del panel de administración con modelos del proyecto

Para demostrar el uso de `django.contrib.admin`, se creó la app **`requerimiento7`**, en la cual se definieron modelos simples y se registraron en el panel de administración para su gestión.

```python
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
    ```