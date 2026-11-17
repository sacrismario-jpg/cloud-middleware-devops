# ☁️ Cloud & Middleware Lab

Laboratorio práctico de infraestructura IT orientado al aprendizaje y aplicación de tecnologías relacionadas con **Linux, Python, middleware, automatización, monitorización y DevOps**.

El proyecto evoluciona progresivamente desde una aplicación web local hacia un entorno de infraestructura más completo, incorporando buenas prácticas de desarrollo, administración de sistemas y despliegue.

## 🎯 Objetivos

- Desarrollar y administrar aplicaciones web con Python y Flask.
- Comprender la arquitectura de aplicaciones y sus componentes.
- Trabajar con servidores web y proxies inversos.
- Automatizar tareas mediante Bash y Python.
- Implementar monitorización y análisis de logs.
- Aplicar control de versiones y pruebas automatizadas.
- Introducir progresivamente herramientas de contenerización y CI/CD.
- Explorar posteriormente arquitecturas desplegadas en cloud.

## 🛠️ Tecnologías

| Tecnología | Utilización |
|---|---|
| Zorin OS 18.1 | Entorno Linux de desarrollo |
| Python 3.12 | Desarrollo de aplicaciones y automatización |
| Flask 3.1.3 | Framework web |
| Pytest 9.2.0 | Pruebas automatizadas |
| Git | Control de versiones |
| GitHub | Repositorio y portfolio técnico |
| Bash | Automatización en Linux |

## 🏗️ Arquitectura actual

La aplicación utiliza una arquitectura modular basada en los patrones **Application Factory** y **Blueprints** de Flask.

```text
cloud-middleware-devops/
│
├── app/
│   ├── __init__.py
│   └── routes.py
│
├── tests/
│   └── test_app.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── run.py
```

### Componentes

- `app/__init__.py`: creación y configuración de la aplicación mediante Application Factory.
- `app/routes.py`: definición y organización de rutas mediante Blueprint.
- `run.py`: punto de entrada de la aplicación.
- `tests/test_app.py`: pruebas automatizadas de la aplicación.

## 🚀 Instalación y ejecución

### Requisitos

- Linux.
- Python 3.12 o superior.
- Git.

### 1. Clonar el repositorio

```bash
git clone https://github.com/sacrismario-jpg/cloud-middleware-devops.git
cd cloud-middleware-devops
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
python -m pip install -r requirements-dev.txt
```

### 5. Ejecutar la aplicación

```bash
python run.py
```

La aplicación estará disponible en:

http://127.0.0.1:5000/

## 🧪 Pruebas automatizadas

El proyecto utiliza Pytest para comprobar el funcionamiento de la aplicación.

Ejecutar las pruebas:

```bash
python -m pytest -v
```

**Estado actual:** 2 pruebas automatizadas superadas.

- Comprobación de respuesta HTTP 200.
- Comprobación del contenido de la respuesta.

## 📋 Hoja de ruta

| Área | Estado |
|---|---|
| Entorno Linux y Python | ✅ Completado |
| Aplicación web Flask | ✅ Completado |
| Application Factory y Blueprint | ✅ Completado |
| Dependencias de desarrollo y producción | ✅ Completado |
| Pruebas automatizadas iniciales | ✅ Completado |
| Ampliación de pruebas | 🔄 Pendiente |
| Logging y gestión de errores | ⏳ Planificado |
| Servidor web y proxy inverso | ⏳ Planificado |
| Contenerización con Docker | ⏳ Planificado |
| Automatización CI/CD | ⏳ Planificado |
| Despliegue en cloud | ⏳ Futuro |

## 🔐 Seguridad y costes

- Desarrollo inicial en entorno local.
- No se almacenan contraseñas, tokens ni claves privadas en el repositorio.
- No se crean recursos cloud facturables sin revisar previamente los costes y autorizar su utilización.

## 📌 Estado del proyecto

Proyecto en desarrollo.

Repositorio público: [cloud-middleware-devops](https://github.com/sacrismario-jpg/cloud-middleware-devops)
