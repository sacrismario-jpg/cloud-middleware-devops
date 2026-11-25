# ☁️ Cloud & Middleware Lab

Laboratorio práctico de infraestructura IT orientado al aprendizaje y aplicación de tecnologías relacionadas con **Linux, Python, middleware, automatización, monitorización y DevOps**.

El proyecto evoluciona progresivamente desde una aplicación web local hacia un entorno de infraestructura más completo, incorporando buenas prácticas de desarrollo, administración de sistemas, pruebas automatizadas y despliegue.

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
| Coverage 7.17.3 | Análisis de cobertura |
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
├── logs/
│  
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

### Componentes principales

- `app/__init__.py`: creación de la aplicación mediante Application Factory, configuración del logging y gestión de excepciones.
- `app/config.py`: configuraciones base, desarrollo y pruebas.
- `app/routes.py`: definición y organización de rutas mediante Blueprint.
- `run.py`: punto de entrada de la aplicación.
- `tests/test_app.py`: pruebas automatizadas.
- `logs/`: almacenamiento de registros de ejecución.

## ⚙️ Configuración por entornos

La aplicación dispone de tres configuraciones:

| Entorno | TESTING | DEBUG |
|---|---|---|
| Configuración base | False | False |
| Testing | True | False |
| Development | False | True |

La fábrica `create_app()` permite utilizar clases de configuración y diccionarios personalizados.

Esta arquitectura facilita la separación de los entornos de desarrollo, pruebas y futuras ejecuciones de producción.

## 🌐 Endpoints disponibles

### Página principal

```http
GET /
```

Devuelve un mensaje de funcionamiento de la aplicación.

### Health Check

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

## 📋 Logging y gestión de errores

La aplicación incorpora un sistema de registros basado en el módulo estándar `logging` de Python y `RotatingFileHandler`.

Funcionalidades implementadas:

- Registro de inicialización de la aplicación.
- Registro automático de peticiones HTTP.
- Identificación del método HTTP, ruta y código de respuesta.
- Rotación automática de archivos de registro.
- Tamaño máximo de 10 KB por archivo.
- Conservación de hasta cinco archivos de respaldo.
- Registro de excepciones inesperadas.
- Captura de traceback para facilitar el diagnóstico.
- Respuestas JSON para errores internos HTTP 500.
- Conservación de los códigos HTTP correspondientes a errores 404 y 405.
- Exclusión del manejador de archivo cuando la aplicación se crea en modo testing.

Los registros se almacenan en:

```text
logs/app.log
```

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

El servidor integrado de Flask se utiliza exclusivamente para desarrollo local. No está destinado a producción.

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

**Estado actual:**

- 14 pruebas automatizadas superadas.
- 100 % de cobertura del paquete `app`.

Las pruebas verifican:

- Respuestas HTTP de la página principal.
- Contenido de las respuestas.
- Métodos HTTP permitidos y no permitidos.
- Respuestas HTTP 404 y 405.
- Funcionamiento del método HEAD.
- Tipos de contenido HTML y JSON.
- Funcionamiento del endpoint `/health`.
- Configuraciones base, testing y development.
- Aplicación de configuraciones personalizadas.
- Gestión de excepciones inesperadas.
- Respuestas HTTP 500.

La cobertura del 100 % corresponde a las instrucciones ejecutables del código actual. No implica que se hayan probado todos los escenarios posibles.

## 📋 Hoja de ruta

| Área | Estado |
|---|---|
| Entorno Linux y Python | ✅ Completado |
| Aplicación web Flask | ✅ Completado |
| Application Factory y Blueprint | ✅ Completado |
| Configuración por entornos | ✅ Completado |
| Endpoint básico de salud | ✅ Completado |
| Logging con rotación | ✅ Completado |
| Registro de peticiones HTTP | ✅ Completado |
| Gestión global de excepciones | ✅ Completado |
| Pruebas automatizadas | ✅ 14 superadas |
| Medición de cobertura | ✅ 100 % |
| Logging específico para testing | 🔄 Implementación inicial |
| Logging estructurado | ⏳ Planificado |
| Gestión avanzada de errores | ⏳ Planificado |
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

Repositorio público:

https://github.com/sacrismario-jpg/cloud-middleware-devops

## Servidor WSGI con Gunicorn

El proyecto incorpora **Gunicorn** como servidor WSGI para ejecutar la aplicación Flask en un entorno distinto al servidor de desarrollo integrado de Flask.

### Instalación

Gunicorn está incluido en `requirements.txt`.

Para instalar las dependencias:

```bash
pip install -r requirements.txt
```

### Configuración

Los parámetros del servidor se encuentran en `gunicorn.conf.py`:

```python
bind = "127.0.0.1:8000"

workers = 2

accesslog = "-"
errorlog = "-"
loglevel = "info"

capture_output = True
```

Configuración utilizada:

- **bind:** escucha en la interfaz local, puerto 8000.
- **workers:** utiliza dos procesos de trabajo.
- **accesslog:** envía los registros de acceso a la salida estándar.
- **errorlog:** envía los registros de errores a la salida de error estándar.
- **loglevel:** establece el nivel de registro informativo.
- **capture_output:** redirige la salida de la aplicación a los registros de errores de Gunicorn.

### Ejecución

Para iniciar la aplicación con Gunicorn:

```bash
gunicorn --config gunicorn.conf.py "app:create_app()"
```

La aplicación queda disponible localmente en:

```text
http://127.0.0.1:8000
```

Para comprobar su funcionamiento:

```bash
curl -i http://127.0.0.1:8000/health
```

La respuesta esperada es HTTP 200:

```json
{
  "status": "ok"
}
```

### Diferencia entre Flask y Gunicorn

- `python run.py`: inicia el servidor de desarrollo integrado de Flask.
- `gunicorn --config gunicorn.conf.py "app:create_app()"`: ejecuta la aplicación mediante un servidor WSGI.

El servidor integrado de Flask se utiliza para desarrollo y pruebas. Gunicorn permite ejecutar la aplicación mediante un servidor WSGI, aunque para un despliegue público todavía habría que configurar aspectos adicionales, como un proxy inverso, HTTPS y controles de seguridad.
