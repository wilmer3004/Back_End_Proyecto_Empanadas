# 🍴 Proyecto Empanada CDM

Aplicación web para la **gestión de ventas e inventarios** de una tienda de empanadas, diseñada con **Flask (Python)**, **PostgreSQL** y un esquema de **API-RESTful**, siguiendo principios de **programación orientada a objetos** y **arquitectura limpia**.

---

## 👥 Autores

* Wilmer Andres Capera
* Felipe Leguizamo
* Maria Fernanda Moya
* Esteban Salvador

Docente: **Mauricio Morales Meneses**
Fecha: **23 de agosto de 2025**

---

## ⚙️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.12
* **Framework Backend:** Flask
* **Base de Datos:** PostgreSQL
* **Entorno:** Virtualenv
* **Gestión de configuración:** Variables de entorno con `python-decouple`
* **Control de versiones:** GitHub con GitFlow

---

## 📂 Estructura del Proyecto

```
📦 Back_End_Proyecto_Empanadas
 ┣ 📂 src
 ┃ ┣ 📂 database      # Configuración de conexión a la base de datos
 ┃ ┣ 📂 models        # Modelos de datos
 ┃ ┣ 📂 routes        # Rutas (endpoints) agrupadas por recurso
 ┃ ┣ 📂 services      # Lógica de negocio
 ┃ ┣ 📂 tests         # Pruebas unitarias e integración
 ┃ ┣ 📂 utils         # Funciones auxiliares y helpers
 ┃ ┗ __init__.py
 ┣ 📜 index.py        # Punto de entrada principal de la aplicación
 ┣ 📜 config.py       # Configuración de entornos
 ┣ 📜 requirements.txt # Dependencias del proyecto
 ┣ 📜 .env            # Variables de entorno
 ┣ 📜 .gitignore
 ┗ 📜 README.md
```

## ▶️ Instalación y Ejecución

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/wilmer3004/Back_End_Proyecto_Empanadas.git
   cd Back_End_Proyecto_Empanadas
   ```

2. **Crear y activar entorno virtual**

   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   source venv/bin/activate       # Linux/Mac
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**

   ```bash
   python index.py
   ```

El servidor quedará disponible en:
👉 `http://127.0.0.1:5000`

---

## 📡 Endpoints (ejemplo)

Actualmente el proyecto cuenta con un módulo de **Personas**:

```
GET     /api/v1/persons           -> Listar personas
POST    /api/v1/persons           -> Registrar persona
PUT     /api/v1/persons/<id>      -> Actualizar persona
DELETE  /api/v1/persons/<id>      -> Eliminar persona
PATCH   /api/v1/persons/<id>/state -> Cambiar estado de persona
```

---



