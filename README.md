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
| Gunicorn 27.0.1 | Servidor WSGI |
| Nginx | Proxy inverso |
| systemd | Gestión del servicio |
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
│   ├── app.log
│   ├── gunicorn-access.log
│   └── gunicorn-error.log
│
├── tests/
│   └── test_app.py
│
├── gunicorn.conf.py
├── run.py
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
└── README.md
```

La configuración de Nginx y el servicio systemd se encuentran en sus ubicaciones correspondientes dentro del sistema operativo, fuera del repositorio.

### Componentes principales

- `app/__init__.py`: creación de la aplicación mediante Application Factory, configuración del logging y gestión de excepciones.
- `app/config.py`: configuraciones base, desarrollo y pruebas.
- `app/routes.py`: definición y organización de rutas mediante Blueprint.
- `run.py`: punto de entrada de la aplicación.
- `tests/test_app.py`: pruebas automatizadas.
- `gunicorn.conf.py`: configuración del servidor WSGI.
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

Los registros de la aplicación Flask se almacenan en:

```text
logs/app.log
```

Gunicorn dispone de archivos independientes para sus registros de acceso y errores:

```text
logs/gunicorn-access.log
logs/gunicorn-error.log
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

```text
http://127.0.0.1:5000/
```

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

## 🦄 Servidor WSGI con Gunicorn

El proyecto incorpora **Gunicorn** como servidor WSGI para ejecutar la aplicación Flask mediante un servidor independiente del servidor de desarrollo integrado.

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

accesslog = "/home/mario/proyectos/cloud-middleware-devops/logs/gunicorn-access.log"
errorlog = "/home/mario/proyectos/cloud-middleware-devops/logs/gunicorn-error.log"

loglevel = "info"

capture_output = True
```

Configuración utilizada:

- **bind:** escucha en la interfaz local, puerto 8000.
- **workers:** utiliza dos procesos de trabajo.
- **accesslog:** almacena los registros de acceso en un archivo.
- **errorlog:** almacena los registros de errores en un archivo.
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

La respuesta esperada es HTTP 200 con el estado `ok`.

## 🌍 Proxy inverso con Nginx

El laboratorio incorpora **Nginx** como proxy inverso situado delante de Gunicorn.

Nginx recibe las peticiones HTTP y las reenvía al servidor WSGI, que ejecuta la aplicación Flask.

### Arquitectura de comunicación

```text
         CLIENTE
            |
            | HTTP :80
            v
        NGINX
     Proxy inverso
            |
            | HTTP :8000
            v
       GUNICORN
       2 workers
            |
            v
         FLASK
      Application
         Factory
            |
            v
       ENDPOINTS
       / y /health
```

### Configuración

Archivo de configuración:

```text
/etc/nginx/sites-available/cloud-middleware-lab
```

Configuración aplicada:

```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

La configuración se habilita mediante un enlace simbólico en:

```text
/etc/nginx/sites-enabled/cloud-middleware-lab
```

### Comprobación

Validar la configuración:

```bash
sudo nginx -t
```

Recargar Nginx:

```bash
sudo systemctl reload nginx
```

Comprobar el endpoint a través del proxy:

```bash
curl -i http://127.0.0.1/health
```

Respuesta esperada:

```http
HTTP/1.1 200 OK
```

```json
{
  "status": "ok"
}
```

**Estado:** Nginx está instalado y activo. La comunicación entre Nginx, Gunicorn y Flask ha sido comprobada satisfactoriamente.

## ⚙️ Gestión del servicio con systemd

El laboratorio incorpora un servicio de **systemd** para gestionar la ejecución de Gunicorn como servicio del sistema.

Esto permite iniciar la aplicación sin necesidad de ejecutar manualmente Gunicorn desde una terminal.

### Configuración del servicio

Archivo:

```text
/etc/systemd/system/cloud-middleware-lab.service
```

El servicio utiliza:

- Usuario dedicado: `cloudlab`.
- Grupo: `cloudlab`.
- Directorio de trabajo: `/home/mario/proyectos/cloud-middleware-devops`.
- Ejecución de Gunicorn desde el entorno virtual del proyecto.
- Reinicio automático ante la finalización del proceso.
- Inicio automático durante el arranque del sistema.

### Gestión del servicio

Recargar la configuración de systemd:

```bash
sudo systemctl daemon-reload
```

Habilitar e iniciar el servicio:

```bash
sudo systemctl enable --now cloud-middleware-lab
```

Consultar su estado:

```bash
sudo systemctl status cloud-middleware-lab --no-pager
```

Detener el servicio:

```bash
sudo systemctl stop cloud-middleware-lab
```

Reiniciar el servicio:

```bash
sudo systemctl restart cloud-middleware-lab
```

Consultar los registros:

```bash
sudo journalctl -u cloud-middleware-lab
```

Seguir los registros en tiempo real:

```bash
sudo journalctl -u cloud-middleware-lab -f
```

### Estado actual

El servicio se encuentra habilitado y funcionando:

```text
cloud-middleware-lab.service
Active: active (running)
Loaded: loaded
enabled
```

La ejecución se realiza mediante el usuario dedicado `cloudlab`, en lugar del usuario personal `mario`.

## 🔐 Seguridad y costes

- Desarrollo y despliegue inicial en entorno local.
- Gunicorn escucha exclusivamente en la interfaz local `127.0.0.1:8000`.
- Nginx recibe las peticiones en el puerto 80.
- El servicio Gunicorn se ejecuta mediante un usuario dedicado.
- No se almacenan contraseñas, tokens ni claves privadas en el repositorio.
- El servidor integrado de Flask no está destinado a producción.
- El laboratorio no dispone todavía de HTTPS ni de una configuración completa de seguridad para exposición pública.
- No se crean recursos cloud facturables sin revisar previamente los costes y autorizar su utilización.

**Importante:** la configuración actual está destinada a un laboratorio local. No debe considerarse un despliegue preparado para exposición pública.

## 📋 Hoja de ruta

| Área | Estado |
|---|---|
| Entorno Linux y Python | ✅ Completado |
| Aplicación web Flask | ✅ Completado |
| Application Factory y Blueprint | ✅ Completado |
| Configuración por entornos | ✅ Completado |
| Endpoint básico de salud (`/health`) | ✅ Completado |
| Logging con rotación de archivos | ✅ Completado |
| Registro de peticiones HTTP | ✅ Completado |
| Gestión global de excepciones | ✅ Completado |
| Pruebas automatizadas | ✅ 14 superadas |
| Medición de cobertura | ✅ 100 % |
| Servidor WSGI Gunicorn | ✅ Completado |
| Proxy inverso con Nginx | ✅ Completado |
| Gestión del servicio con systemd | ✅ Completado |
| Ejecución con usuario dedicado | ✅ Completado |
| Aislamiento del logging en pruebas | 🔄 Implementación inicial |
| Logging estructurado (JSON) | ⏳ Planificado |
| Gestión avanzada de errores | ⏳ Planificado |
| HTTPS y endurecimiento de seguridad | ⏳ Planificado |
| Monitorización de infraestructura | ⏳ Planificado |
| Contenerización con Docker | ⏳ Planificado |
| Automatización CI/CD | ⏳ Planificado |
| Despliegue en la nube | 🔮 Futuro |

## 📌 Estado del proyecto

Proyecto en desarrollo.

Actualmente dispone de una aplicación Flask funcional, pruebas automatizadas, servidor WSGI Gunicorn, proxy inverso Nginx y gestión del servicio mediante systemd.

La arquitectura permite ejecutar el laboratorio como un servicio local persistente y constituye una base para continuar trabajando en administración de sistemas, middleware, monitorización y DevOps.

Repositorio público:

https://github.com/sacrismario-jpg/cloud-middleware-devops
