# Cloud & Middleware Lab

## Objetivo

Construir un laboratorio práctico de infraestructura IT para aprender administración de sistemas, middleware, automatización, monitorización y fundamentos de DevOps.

## Alcance inicial

La primera versión se ejecutará localmente en Zorin OS, sin dependencias obligatorias de servicios cloud de pago.

El proyecto evolucionará progresivamente para incorporar:

- Una aplicación web sencilla con Flask.
- Un servidor web y proxy inverso.
- Automatización mediante Bash y Python.
- Control de versiones con Git.
- Monitorización y análisis de logs.
- Pruebas automatizadas y fundamentos de CI/CD.
- Una posible extensión a AWS o Google Cloud Platform.

## Entorno de desarrollo

- Sistema operativo: Zorin OS 18.1.
- Arquitectura: x86_64.
- Memoria RAM: 8 GB.
- Python: 3.12.3.
- Bash: 5.2.21.

## Arquitectura actual

La aplicación utiliza una estructura modular basada en el patrón Application Factory de Flask y Blueprints.

```text
cloud-middleware-devops/
├── app/
│   ├── __init__.py
│   └── routes.py
├── tests/
│   └── test_app.py
├── .gitignore
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── run.py
```

- `app/__init__.py`: crea y configura la aplicación Flask.
- `app/routes.py`: define las rutas mediante un Blueprint.
- `run.py`: punto de entrada para iniciar el servidor.
- `tests/test_app.py`: contiene las pruebas automatizadas.

## Instalación y ejecución

Activar el entorno virtual:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
python -m pip install -r requirements-dev.txt
```

Iniciar la aplicación:

```bash
python run.py
```

La aplicación estará disponible en:

```text
http://127.0.0.1:5000/
```

## Pruebas automatizadas

Ejecutar las pruebas:

```bash
python -m pytest -v
```

## Estado del proyecto

- [x] Crear estructura inicial.
- [x] Configurar Git.
- [x] Crear entorno virtual Python.
- [x] Instalar Flask.
- [x] Implementar aplicación web inicial.
- [x] Configurar Pytest.
- [x] Crear pruebas automatizadas.
- [x] Separar dependencias de producción y desarrollo.
- [x] Mejorar arquitectura mediante Application Factory y Blueprint.
- [ ] Ampliar pruebas automatizadas.
- [ ] Incorporar logging y gestión de errores.
- [ ] Contenerizar con Docker.
- [ ] Implementar integración continua.
- [ ] Explorar despliegue cloud.

## Seguridad y costes

El desarrollo inicial se realizará en local.

No se crearán recursos cloud facturables sin revisar previamente los costes y confirmar expresamente su utilización.

No se deben almacenar contraseñas, tokens ni claves privadas en el repositorio.

## Documentación

La arquitectura, las decisiones técnicas, las pruebas y los procedimientos de resolución de incidencias se documentarán progresivamente en el directorio `docs/`.
