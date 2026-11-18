# ☁️ Cloud & Middleware Lab

Laboratorio práctico de infraestructura IT orientado al aprendizaje y aplicación de tecnologías relacionadas con **Linux, Python, middleware, automatización, monitorización y DevOps**.

El proyecto evoluciona progresivamente desde una aplicación web local hacia un entorno de infraestructura más completo, incorporando buenas prácticas de desarrollo, administración de sistemas, pruebas y despliegue.

## 🎯 Objetivos

- Desarrollar y administrar aplicaciones web con Python y Flask.
- Comprender la arquitectura de aplicaciones y sus componentes.
- Trabajar con servidores web y proxies inversos.
- Automatizar tareas mediante Bash y Python.
- Implementar monitorización y análisis de logs.
- Aplicar control de versiones y pruebas automatizadas.
- Introducir herramientas de contenerización y CI/CD.
- Explorar posteriormente arquitecturas desplegadas en cloud.

## 🛠️ Tecnologías

| Tecnología | Utilización |
|---|---|
| Zorin OS 18.1 | Entorno Linux de desarrollo |
| Python 3.12.3 | Desarrollo de aplicaciones y automatización |
| Flask 3.1.3 | Framework web |
| Pytest 9.2.0 | Pruebas automatizadas |
| pytest-cov 7.1.0 | Medición de cobertura |
| Coverage 7.17.3 | Análisis de cobertura de código |
| Git | Control de versiones |
| GitHub | Repositorio y portfolio técnico |

Bash está contemplado para futuras tareas de automatización.

## 🏗️ Arquitectura actual

La aplicación utiliza una arquitectura modular basada en los patrones **Application Factory** y **Blueprints** de Flask.

```text
cloud-middleware-devops/
│
├── app/
│   ├── __init__.py
│   ├── config.py
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

- `app/__init__.py`: creación de la aplicación mediante Application Factory y carga de configuraciones.
- `app/config.py`: configuraciones base, desarrollo y pruebas.
- `app/routes.py`: definición de rutas mediante Blueprint y endpoint de salud.
- `run.py`: punto de entrada de la aplicación.
- `tests/test_app.py`: pruebas automatizadas.

### Configuración de la aplicación

Se han implementado tres configuraciones:

| Entorno | TESTING | DEBUG |
|---|---|---|
| Base | False | False |
| Testing | True | False |
| Development | False | True |

La fábrica `create_app()` admite tanto clases de configuración como diccionarios personalizados.

### Endpoint de salud

La aplicación incorpora un endpoint:

```http
GET /health
```

Respuesta:

```json
{
  "status": "ok"
}
```

Devuelve HTTP 200 y contenido JSON.

Actualmente es una comprobación básica de disponibilidad HTTP. Todavía no verifica dependencias externas como bases de datos u otros servicios.

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

Medir la cobertura:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

**Estado actual: 13 pruebas superadas y 100 % de cobertura del paquete `app`.**

Las pruebas verifican:

- Respuesta HTTP 200 de la página principal.
- Contenido de la respuesta.
- Respuesta HTTP 405 ante métodos no permitidos.
- Respuesta HTTP 404 para rutas inexistentes.
- Comportamiento del método HEAD.
- Tipo de contenido HTML.
- Funcionamiento del endpoint `/health`.
- Respuesta JSON y tipo de contenido del endpoint.
- Configuración personalizada.
- Configuraciones base, testing y development.

La cobertura del 100 % corresponde a las instrucciones ejecutables del código actual. No implica que se hayan probado todos los escenarios posibles.

## 📋 Hoja de ruta

| Área | Estado |
|---|---|
| Entorno Linux y Python | ✅ Completado |
| Aplicación web Flask | ✅ Completado |
| Application Factory y Blueprint | ✅ Completado |
| Configuración por entornos | ✅ Completado |
| Endpoint básico de salud | ✅ Completado |
| Dependencias de desarrollo | ✅ Completado |
| Pruebas automatizadas | ✅ 13 pruebas superadas |
| Medición de cobertura | ✅ 100 % |
| Logging y gestión de errores | ⏳ Planificado |
| Servidor web y proxy inverso | ⏳ Planificado |
| Contenerización con Docker | ⏳ Planificado |
| Automatización CI/CD | ⏳ Planificado |
| Despliegue en cloud | ⏳ Futuro |

## 🔐 Seguridad y costes

- Desarrollo inicial en entorno local.
- No se almacenan contraseñas, tokens ni claves privadas en el repositorio.
- El servidor de desarrollo no está destinado a producción.
- No se crean recursos cloud facturables sin revisar previamente los costes y autorizar su utilización.

## 📌 Estado del proyecto

Proyecto en desarrollo.

Repositorio público: https://github.com/sacrismario-jpg/cloud-middleware-devops
