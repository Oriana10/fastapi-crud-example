# FastAPI CRUD Example

Este es un ejemplo de aplicación CRUD usando FastAPI, SQLAlchemy y SQLite. Incluye pruebas unitarias y un pipeline CI/CD en GitHub Actions.

## Requisitos

- Python 3.9+
- FastAPI
- SQLAlchemy

## Cómo usar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest tests/tests_crud.py
```

## Estructura de Archivos

```
fastapi-crud-example/
├── app/
│   ├── main.py            # Archivo principal de FastAPI
│   ├── models.py          # Definición de modelos (Pydantic / ORM)
│   ├── crud.py            # Operaciones CRUD
│   ├── database.py        # Conexión a la base de datos
│   ├── schemas.py         # Esquemas Pydantic
│   ├── tests/
│   │   ├── test_crud.py   # Pruebas unitarias para el CRUD
│   └── Dockerfile         # Dockerfile para el contenedor
├── .github/
│   └── workflows/
│       └── ci.yml         # Pipeline de GitHub Actions
├── requirements.txt       # Dependencias del proyecto
├── requirements-dev.txt   # Dependencias para desarrollo y testing
└── README.md              # Descripción del proyecto
```
