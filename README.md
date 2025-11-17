# FastAPI

<p align="center"> <a href="https://fastapi.tiangolo.com" target="_blank"> <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="220" alt="FastAPI Logo" /> </a> </p>

API REST DE AGROCARE
## Tecnologias

<p align="center"> <img src="https://img.shields.io/badge/python-3.11-blue?logo=python" /> <img src="https://img.shields.io/badge/fastapi-0.115.0-teal?logo=fastapi" /> <img src="https://img.shields.io/badge/uvicorn-0.30.0-purple?logo=uvicorn" /> <img src="https://img.shields.io/badge/pydantic-2.x-green?logo=pydantic" /> </p>

---

| Paquete             | Versión | Descripción                                                          |
| ------------------- | ------- | -------------------------------------------------------------------- |
| `fastapi`           | 0.115.x | Framework web para crear APIs rápidas, tipadas y con validación.     |
| `uvicorn`           | 0.30.x  | Servidor ASGI para ejecutar aplicaciones FastAPI.                    |
| `pydantic`          | 2.x     | Validación de datos y creación de modelos (schemas).                 |
| `typing`            | nativo  | Tipado estático para funciones y modelos.                            |
| `enum`              | nativo  | Manejo de enumeraciones, usado en `GenreEnum`.                       |
| `datetime`          | nativo  | Restricciones dinámicas para validar el año de la película.          |
| `fastapi.responses` | nativo  | Envío de respuestas personalizadas (`JSONResponse`, `FileResponse`). |
| `fastapi.routing`   | nativo  | Modularización mediante `APIRouter`.                                 |

## Instruccion de ejecucion

1. Version de python **Python 3.14**

2. Clonar el repositorio

```
https://github.com/WilcarOrtiz/AgroCare_API.git
```

3.  Crear entorno virtual

```
python -m venv venv
```

4. Activar entorno virtual

```
.\venv\Scripts\activate
```

recuerda selecionar el interprete

5. Instalar paquetes

```
pip install -r requirements.txt
```

6. verificar instalacion de paquetes

```
pip list
```

7. Ejecutar el docker compose
```
docker-compose up -d
```

8. correr FastAPI
```
uvicorn src.main:app --port 5000 --host 0.0.0.0 --reload
```
