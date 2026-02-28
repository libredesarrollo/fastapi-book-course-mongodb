# FastAPI con MongoDB y Motor

Este repositorio contiene un ejemplo práctico de cómo implementar una API RESTful asíncrona utilizando **FastAPI** y **MongoDB**, haciendo uso del driver **Motor**.

Este código forma parte del curso: [Primeros pasos con FastAPI](https://www.desarrollolibre.net/blog/python/curso-primeros-pasos-con-fastapi) de Desarrollo Libre.

## 🚀 Tecnologías

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno y de alto rendimiento para construir APIs con Python.
- **[MongoDB](https://www.mongodb.com/)**: Base de datos NoSQL orientada a documentos.
- **[Motor](https://motor.readthedocs.io/)**: Driver asíncrono de Python para MongoDB.
- **[Pydantic](https://docs.pydantic.dev/)**: Validación de datos y gestión de esquemas.

## 📋 Requisitos

- Python 3.8+
- Una instancia de MongoDB ejecutándose (por defecto en `localhost:27017`).

## 🛠️ Instalación

1. **Clona el repositorio:**

   ```bash
   git clone <url-de-tu-repo>
   cd <nombre-de-tu-repo>
   ```

2. **Instala las dependencias:**

   Se recomienda utilizar un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install fastapi uvicorn motor pymongo
   ```

## ▶️ Ejecución

Navega a la carpeta `database` y ejecuta el servidor con Uvicorn:

```bash
cd database
uvicorn api:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`.

## 📚 Documentación Interactiva

FastAPI genera automáticamente documentación interactiva para probar la API:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🍃 Endpoints de MongoDB

La lógica de MongoDB se encuentra en `mongo_task.py` y se expone bajo el prefijo `/mongo/tasks`.

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/mongo/tasks/` | Crear una nueva tarea. |
| `GET` | `/mongo/tasks/` | Obtener todas las tareas. |
| `GET` | `/mongo/tasks/{id}` | Obtener una tarea por su ID. |
| `PUT` | `/mongo/tasks/{id}` | Actualizar una tarea completa. |
| `PUT` | `/mongo/tasks/{id}/category` | Actualizar solo la categoría de una tarea. |
| `PUT` | `/mongo/tasks/{id}/tags/add` | Añadir etiquetas a una tarea (sin duplicados). |
| `PUT` | `/mongo/tasks/{id}/tags/remove` | Eliminar etiquetas de una tarea. |
| `DELETE` | `/mongo/tasks/{id}` | Eliminar una tarea. |
