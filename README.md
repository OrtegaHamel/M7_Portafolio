# 📘 M7_Evaluación de portafolio
Por Álvaro Ortega Hamel

Este repositorio contiene un ejercicio integral diseñado para demostrar las capacidades del framework **Django** en la gestión de datos, modelado, migraciones y patrones de diseño MVC.

El proyecto está estructurado de manera modular, donde **cada requerimiento se encuentra en una aplicación (app) independiente**, facilitando el estudio aislado de cada funcionalidad.

---

## ⚙️ Guía de Instalación y Ejecución

Sigue estos pasos para configurar el proyecto en tu entorno local.

### 1. Clonar el repositorio
Descarga el código fuente a tu máquina local:
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>
```

### 2. Crear y activar entorno virtual
Es recomendable usar un entorno virtual para aislar las dependencias:

**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
Instala Django y las librerías necesarias:
```bash
pip install django
# Si tienes un archivo requirements.txt:
# pip install -r requirements.txt
```

### 4. Configuración de la Base de Datos y Migraciones
El proyecto utiliza **SQLite** por defecto. Para inicializar la base de datos y crear las tablas de todas las apps (requerimientos), ejecuta:

```bash
# Crea los archivos de migración para los cambios en los modelos
python manage.py makemigrations

# Aplica las migraciones a la base de datos (crea las tablas)
python manage.py migrate
```

### 5. Crear Superusuario
Para acceder al panel de administración (Requerimiento 7):
```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor
Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```
Accede al proyecto en: `http://127.0.0.1:8000/`

---

## 📂 Estructura del Proyecto

A continuación se describen los módulos incluidos en este proyecto:

### 1️⃣ Conceptos Fundamentales (`requerimiento1`)
Documentación y ejemplos teóricos sobre cómo Django se integra con bases de datos.
* **Temas:** ORM, Soporte Multi-DB (SQLite, PostgreSQL, MySQL), manejo de conexiones y transacciones.
* **Objetivo:** Comprender la abstracción que realiza Django sobre SQL.

### 2️⃣ Modelos Independientes (`requerimiento2`)
Implementación de la capa de acceso a datos utilizando entidades no relacionadas.
* **Modelo:** `Producto` (Nombre, Precio, Cantidad).
* **Objetivo:** Crear tablas independientes sin claves foráneas.

### 3️⃣ Relaciones entre Modelos (`requerimiento3`)
Modelado de entidades interconectadas utilizando los tipos de relación estándar de Django.
* **Modelos:**
    * `Cliente` ↔ `PerfilCliente` (**Uno a Uno**)
    * `Cliente` ↔ `Pedido` (**Uno a Muchos**)
    * `Pedido` ↔ `Producto` (**Muchos a Muchos**)
* **Objetivo:** Representar estructuras de datos complejas y relacionales.

### 4️⃣ Sistema de Migraciones (`requerimiento4`)
Demostración del flujo de trabajo para propagar cambios en los modelos hacia la base de datos.
* **Caso Práctico:** Creación del modelo `ProductoDemo` y la posterior adición del campo `precio` mediante una migración (`makemigrations` y `migrate`).
* **Objetivo:** Mantener la integridad del esquema de base de datos evolutivo.

### 5️⃣ Consultas Avanzadas y ORM (`requerimiento5`)
Uso de métodos avanzados del ORM para recuperación selectiva de información.
* **Funcionalidad:** Filtrado de pedidos por cliente específico en un rango de fechas.
* **Métodos clave:** `filter()`, `get()`, `__range` (SQL BETWEEN).
* **Ubicación lógica:** `requerimiento5/queries.py`.

### 6️⃣ Aplicación CRUD - MVC (`requerimiento6`)
Implementación completa de una aplicación web siguiendo el patrón Modelo-Vista-Controlador.
* **Funcionalidad:** Sistema de Gestión de Productos.
* **Operaciones:**
    * **C**reate (Crear productos)
    * **R**ead (Listar productos)
    * **U**pdate (Editar productos)
    * **D**elete (Eliminar productos)
* **Componentes:** Vistas (`views.py`), URLs (`urls.py`), Formularios (`forms.py`) y Templates.

### 7️⃣ Aplicaciones Preinstaladas (`requerimiento7`)
Exploración y configuración de las herramientas "baterías incluidas" de Django.
* **Apps analizadas:** `django.contrib.admin`, `auth`, `sessions`, `messages`.
* **Implementación:** Registro de modelos `Categoria` y `Articulo` en el panel de administración para su gestión visual.

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Framework:** Django 4.x / 5.x
* **Base de Datos:** PostgreSQL
* **Frontend:** HTML5, CSS3 (Templates de Django)

---

## 📝 Notas Adicionales
Para probar las consultas del **Requerimiento 5**, puedes utilizar la shell de Django:

```bash
python manage.py shell
>>> from requerimiento5.queries import ejemplo_consulta_pedidos_cliente
>>> ejemplo_consulta_pedidos_cliente()
```

---
**Desarrollado como ejercicio práctico de integración de Django.**