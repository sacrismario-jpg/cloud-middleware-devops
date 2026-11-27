# ☁️ Cloud & Middleware Lab

Laboratorio práctico de infraestructura IT orientado al aprendizaje y aplicación de tecnologías relacionadas con **Linux, Python, middleware, automatización, monitorización, contenerización y DevOps**.

El proyecto evoluciona desde una aplicación web local hasta un entorno de despliegue contenerizado, incorporando buenas prácticas de desarrollo, administración de sistemas, seguridad, pruebas automatizadas e integración continua.

## 🎯 Objetivos

- Desarrollar y administrar aplicaciones web con Python y Flask.
- Comprender la arquitectura de aplicaciones y sus componentes.
- Trabajar con servidores WSGI y proxies inversos.
- Administrar servicios Linux mediante systemd.
- Implementar logging estructurado y gestión de errores.
- Automatizar pruebas y comprobar la cobertura del código.
- Contenerizar aplicaciones mediante Docker.
- Gestionar servicios y redes con Docker Compose.
- Aplicar medidas de seguridad y aislamiento en contenedores.
- Implementar integración continua mediante GitHub Actions.
- Explorar posteriormente arquitecturas desplegadas en cloud.

## 🛠️ Tecnologías

| Tecnología | Utilización |
|---|---|
| Zorin OS 18.1 | Entorno Linux de desarrollo |
| Python 3.12 | Desarrollo de aplicaciones y automatización |
| Flask 3.1.3 | Framework web |
| Gunicorn 27.0.1 | Servidor WSGI |
| Nginx | Proxy inverso |
| systemd | Gestión y supervisión de servicios |
| Docker Engine | Contenerización |
| Docker Compose | Orquestación de contenedores |
| Pytest 9.2.0 | Pruebas automatizadas |
| pytest-cov 7.1.0 | Medición de cobertura |
| Git | Control de versiones |
| GitHub | Repositorio y portfolio técnico |
| GitHub Actions | Integración continua |
| Linux | Administración del entorno |

## 🏗️ Arquitectura del proyecto

La aplicación utiliza una arquitectura modular basada en los patrones **Application Factory** y **Blueprints** de Flask.

La infraestructura dispone de dos modalidades de ejecución:

1. Despliegue tradicional sobre Linux mediante Gunicorn, Nginx y systemd.
2. Despliegue contenerizado mediante Docker Compose.

### Arquitectura Docker Compose

```text
                  CLIENTE
                     |
                     | HTTP
                     v
          +----------------------+
          |        NGINX         |
          |  Reverse Proxy       |
          |  Puerto 8080         |
          |  Usuario no root     |
          +----------------------+
                     |
                     | Red interna Docker
                     | app:8000
                     v
          +----------------------+
          |       GUNICORN       |
          |      2 workers       |
          |                      |
          |       FLASK          |
          |   Aplicación web     |
          +----------------------+
                     |
                     v
              /health
              /ready
```

Nginx recibe las peticiones HTTP y las reenvía a Gunicorn mediante la red interna de Docker.

El servicio Flask no publica directamente ningún puerto en el host. El acceso se realiza a través del proxy inverso.

### Estructura del repositorio

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
├── docker/
│   └── nginx/
│       └── default.conf
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── gunicorn.conf.py
├── gunicorn.docker.conf.py
├── run.py
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
└── README.md
```

### Componentes principales

- `app/__init__.py`: Application Factory, configuración del logging, identificación de peticiones y gestión de excepciones.
- `app/config.py`: configuraciones base, desarrollo y pruebas.
- `app/routes.py`: definición de rutas mediante Blueprint.
- `tests/test_app.py`: pruebas automatizadas.
- `Dockerfile`: construcción de la imagen de la aplicación.
- `compose.yaml`: definición y configuración de los servicios Docker.
- `docker/nginx/default.conf`: configuración del proxy inverso.
- `gunicorn.conf.py`: configuración de Gunicorn para el despliegue tradicional.
- `gunicorn.docker.conf.py`: configuración de Gunicorn para Docker.
- `.github/workflows/ci.yml`: pipeline de integración continua.
- `.dockerignore`: exclusión de archivos innecesarios durante la construcción de imágenes.

## ⚙️ Configuración de la aplicación

La aplicación dispone de tres configuraciones:

| Entorno | TESTING | DEBUG |
|---|---|---|
| Configuración base | False | False |
| Testing | True | False |
| Development | False | True |

La fábrica `create_app()` permite utilizar clases de configuración y diccionarios personalizados.

Esta arquitectura facilita la separación de los entornos de desarrollo, pruebas y ejecución del servicio.

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

Devuelve HTTP 200 y comprueba que la aplicación responde a las peticiones.

### Readiness Check

```http
GET /ready
```

Respuesta:

```json
{
  "status": "ready"
}
```

Devuelve HTTP 200 e indica que la aplicación está preparada para atender peticiones.

Actualmente ambos endpoints realizan comprobaciones básicas de la aplicación. No verifican dependencias externas como bases de datos u otros servicios.

## 📋 Logging y gestión de errores

La aplicación utiliza el módulo estándar `logging` de Python y un formateador personalizado `JSONFormatter`.

### Funcionalidades implementadas

- Registro de inicialización de la aplicación.
- Registro automático de peticiones HTTP.
- Identificación del método HTTP, ruta y código de respuesta.
- Identificador único por petición mediante UUID.
- Inclusión de `X-Request-ID` en las respuestas HTTP.
- Registro de excepciones inesperadas.
- Captura de información de diagnóstico.
- Respuestas JSON para errores internos HTTP 500.
- Conservación de los códigos HTTP correspondientes a errores 404 y 405.
- Rotación automática de archivos de registro en el despliegue tradicional.
- Salida de registros por stdout en el despliegue contenerizado.

### Formato JSON

Los registros estructurados pueden incluir:

- Timestamp UTC.
- Nivel del registro.
- Nombre del logger.
- Mensaje.
- Módulo y función.
- Número de línea.
- Identificador de petición.
- Método HTTP.
- Ruta.
- Código de respuesta.
- Información de excepciones.

### Modos de logging

**Despliegue tradicional:**

Se utiliza `RotatingFileHandler` con un tamaño máximo de 10 KB y hasta cinco archivos de respaldo.

Los registros se almacenan en:

```text
logs/app.log
```

Gunicorn dispone de archivos independientes:

```text
logs/gunicorn-access.log
logs/gunicorn-error.log
```

**Despliegue Docker:**

Se utiliza la variable de entorno:

```text
LOG_TO_STDOUT=1
```

Los registros se envían a la salida estándar para facilitar su consulta mediante Docker.

## 🧪 Pruebas automatizadas

El proyecto utiliza Pytest y pytest-cov para verificar el funcionamiento de la aplicación y medir la cobertura del código.

### Ejecutar las pruebas

```bash
python -m pytest -v
```

### Medir la cobertura

```bash
python -m pytest \
  --cov=app \
  --cov-report=term-missing
```

### Validar el umbral mínimo de cobertura

```bash
python -m pytest \
  --cov=app \
  --cov-report=term-missing \
  --cov-fail-under=100
```

### Estado actual

- **19 pruebas automatizadas superadas.**
- **100 % de cobertura del paquete `app`.**

Las pruebas verifican:

- Respuestas HTTP de la página principal.
- Métodos HTTP permitidos y no permitidos.
- Respuestas HTTP 404 y 405.
- Funcionamiento del método HEAD.
- Tipos de contenido HTML y JSON.
- Endpoints `/health` y `/ready`.
- Identificador único de petición.
- Configuraciones base, testing y development.
- Aplicación de configuraciones personalizadas.
- Gestión de excepciones inesperadas.
- Respuestas HTTP 500.
- Configuración del logging JSON por stdout.
- Configuración del logging tradicional mediante RotatingFileHandler.

La cobertura del 100 % corresponde a las instrucciones ejecutables del código actual. No implica que se hayan probado todos los escenarios posibles.

## 🦄 Servidor WSGI con Gunicorn

Gunicorn se utiliza como servidor WSGI para ejecutar la aplicación Flask mediante un servidor independiente del servidor de desarrollo integrado.

### Despliegue tradicional

La configuración se encuentra en:

```text
gunicorn.conf.py
```

Características principales:

- Dos procesos worker.
- Escucha en `127.0.0.1:8000`.
- Registro independiente de accesos y errores.
- Captura de la salida estándar y de errores.

Ejecución manual:

```bash
gunicorn --config gunicorn.conf.py "app:create_app()"
```

### Despliegue Docker

Se utiliza una configuración independiente:

```text
gunicorn.docker.conf.py
```

Gunicorn escucha en `0.0.0.0:8000` dentro del contenedor, permitiendo que Nginx acceda a la aplicación a través de la red interna de Docker.

## 🌐 Nginx como proxy inverso

Nginx actúa como servidor web y proxy inverso.

Se han implementado dos configuraciones:

- Instalación tradicional en el sistema Linux.
- Contenedor Nginx independiente dentro de Docker Compose.

### Nginx tradicional

La configuración del sistema se encuentra en:

```text
/etc/nginx/sites-available/cloud-middleware-lab
```

Recibe peticiones HTTP en el puerto 80 y las reenvía a Gunicorn en `127.0.0.1:8000`.

Validación:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

### Nginx en Docker

La configuración se encuentra en:

```text
docker/nginx/default.conf
```

Características:

- Imagen `nginxinc/nginx-unprivileged:alpine`.
- Ejecución con usuario no privilegiado.
- Puerto interno 8080.
- Comunicación con Flask mediante el nombre de servicio `app`.
- Logs de acceso y errores enviados a stdout y stderr.
- Configuración montada en modo solo lectura.

## ⚙️ Gestión del servicio con systemd

Se ha configurado un servicio de systemd para gestionar Gunicorn como servicio del sistema.

Archivo:

```text
/etc/systemd/system/cloud-middleware-lab.service
```

El servicio utiliza un usuario dedicado llamado `cloudlab`.

### Gestión del servicio

```bash
# Recargar configuración
sudo systemctl daemon-reload

# Iniciar y habilitar
sudo systemctl enable --now cloud-middleware-lab

# Consultar estado
sudo systemctl status cloud-middleware-lab

# Reiniciar
sudo systemctl restart cloud-middleware-lab

# Detener
sudo systemctl stop cloud-middleware-lab

# Consultar registros
sudo journalctl -u cloud-middleware-lab
```

El servicio está configurado para iniciarse automáticamente con el sistema y reiniciarse si se produce un fallo.

## 🔐 Seguridad y endurecimiento

Se han aplicado medidas de seguridad tanto en el servicio tradicional como en los contenedores Docker.

### Seguridad en systemd

La aplicación tradicional se ejecuta mediante el usuario específico `cloudlab`, evitando utilizar root para ejecutar Gunicorn.

Se han aplicado directivas de endurecimiento mediante:

```text
/etc/systemd/system/cloud-middleware-lab.service.d/override.conf
```

Entre las medidas implementadas:

- `NoNewPrivileges`.
- `UMask`.
- `PrivateTmp`.
- `ProtectSystem`.
- `ProtectKernelTunables`.
- `ProtectKernelModules`.
- `ProtectKernelLogs`.
- `ProtectControlGroups`.
- `ProtectHostname`.
- `ProtectClock`.
- `RestrictSUIDSGID`.
- `LockPersonality`.
- `PrivateDevices`.
- `ProtectProc`.
- `ProcSubset`.
- `RestrictNamespaces`.
- `RestrictRealtime`.
- `SystemCallArchitectures`.
- `CapabilityBoundingSet`.
- `AmbientCapabilities`.
- `RestrictAddressFamilies`.
- `MemoryDenyWriteExecute`.

Evaluación:

```bash
sudo systemd-analyze security cloud-middleware-lab.service
```

Resultado obtenido: **3.1 OK**.

Esta puntuación corresponde a la evaluación de systemd y no constituye una auditoría completa de seguridad.

### Seguridad en Docker

Los contenedores se han configurado aplicando medidas de reducción de privilegios y aislamiento.

**Aplicación Flask:**

- Usuario no privilegiado `appuser`.
- Sistema de archivos raíz de solo lectura.
- Capacidades Linux eliminadas mediante `cap_drop: ALL`.
- Protección `no-new-privileges`.
- Directorio temporal limitado mediante tmpfs.
- Límite de memoria de 256 MB.
- Límite de CPU de 1 núcleo.
- Límite de 100 procesos.
- Sin publicación directa de puertos en el host.

**Nginx:**

- Imagen basada en `nginx-unprivileged`.
- Usuario no privilegiado.
- Sistema de archivos raíz de solo lectura.
- Capacidades Linux eliminadas mediante `cap_drop: ALL`.
- Protección `no-new-privileges`.
- Directorio temporal limitado mediante tmpfs.
- Límite de memoria de 64 MB.
- Límite de CPU de 0,5 núcleos.
- Límite de 50 procesos.
- Puerto publicado exclusivamente en `127.0.0.1:8080`.

Estas medidas reducen la superficie de ataque y limitan el impacto potencial de una ejecución comprometida.

## 🐳 Contenerización con Docker

La aplicación se ha contenerizado mediante un Dockerfile basado en:

```dockerfile
FROM python:3.12-slim
```

### Características de la imagen

- Imagen base Python slim.
- Instalación de dependencias mediante `requirements.txt`.
- Ejecución con usuario no privilegiado.
- Gunicorn como servidor WSGI.
- Logging estructurado por stdout.
- Healthcheck mediante el endpoint `/health`.
- Exclusión de archivos innecesarios mediante `.dockerignore`.

### Construir la imagen

```bash
sudo docker build -t cloud-middleware-lab:latest .
```

### Ejecutar Docker Compose

El proyecto utiliza Docker Compose para gestionar los servicios Flask y Nginx.

Levantar los servicios:

```bash
sudo docker compose up -d --build
```

Consultar el estado:

```bash
sudo docker compose ps
```

Consultar los registros:

```bash
sudo docker compose logs -f
```

Consultar los registros de Flask:

```bash
sudo docker compose logs -f app
```

Consultar los registros de Nginx:

```bash
sudo docker compose logs -f nginx
```

Detener los servicios:

```bash
sudo docker compose down
```

### Acceso a la aplicación

Una vez levantados los contenedores:

```text
http://127.0.0.1:8080/
```

Comprobar los endpoints:

```bash
curl -i http://127.0.0.1:8080/health
curl -i http://127.0.0.1:8080/ready
```

Los servicios se comunican mediante una red bridge de Docker.

Nginx publica el puerto 8080 únicamente en la interfaz local del host, mientras que Flask permanece accesible solo dentro de la red interna de los contenedores.

## 🔄 Integración continua con GitHub Actions

El repositorio incorpora un pipeline de integración continua mediante GitHub Actions.

Archivo:

```text
.github/workflows/ci.yml
```

El workflow se ejecuta cuando se producen:

- Push a la rama `main`.
- Pull requests dirigidas a `main`.

### Fases del pipeline

```text
       PUSH / PULL REQUEST
                |
                v
       +------------------+
       |     CHECKOUT     |
       | Descargar código|
       +------------------+
                |
                v
       +------------------+
       |  SETUP PYTHON    |
       |     Python 3.12  |
       +------------------+
                |
                v
       +------------------+
       |   DEPENDENCIAS   |
       | Instalar paquetes|
       +------------------+
                |
                v
       +------------------+
       |      PYTEST      |
       | 19 pruebas       |
       | Cobertura 100 %  |
       +------------------+
                |
                v
       +------------------+
       |   DOCKER BUILD   |
       | Construir imagen |
       +------------------+
                |
                v
          CI COMPLETADA
```

### Comprobaciones implementadas

1. Descarga del repositorio.
2. Preparación de Python 3.12.
3. Instalación de dependencias.
4. Ejecución de pruebas automatizadas.
5. Validación de cobertura mínima del 100 %.
6. Construcción de la imagen Docker.

### Resultado validado

Primera ejecución satisfactoria:

- Commit: `77b98be`.
- Workflow: `Cloud Middleware Lab CI`.
- Resultado: Success.
- Duración aproximada: 18 segundos.

El pipeline valida automáticamente las pruebas y la construcción de la imagen.

**Nota:** actualmente se ha implementado integración continua (CI). No se ha implementado todavía un proceso de despliegue continuo (CD).

## 📊 Estado actual del proyecto

| Área | Estado |
|---|---|
| Entorno Linux y Python | ✅ Completado |
| Aplicación Flask | ✅ Completado |
| Application Factory y Blueprints | ✅ Completado |
| Configuración por entornos | ✅ Completado |
| Endpoints Health y Readiness | ✅ Completado |
| Logging estructurado JSON | ✅ Completado |
| Identificación de peticiones | ✅ Completado |
| Gestión global de excepciones | ✅ Completado |
| Pruebas automatizadas | ✅ Completado |
| Cobertura del 100 % | ✅ Completado |
| Gunicorn | ✅ Completado |
| Nginx como proxy inverso | ✅ Completado |
| Servicio systemd | ✅ Completado |
| Endurecimiento de systemd | ✅ Completado |
| Dockerfile | ✅ Completado |
| Docker Compose | ✅ Completado |
| Endurecimiento de contenedores | ✅ Completado |
| GitHub Actions CI | ✅ Completado |
| Validación del pipeline remoto | ✅ Completado |

## 🗺️ Hoja de ruta

El laboratorio continuará evolucionando de forma progresiva.

| Área | Estado |
|---|---|
| Administración Linux | ✅ Completado |
| Aplicación Flask modular | ✅ Completado |
| Logging y gestión de errores | ✅ Completado |
| Pruebas automatizadas | ✅ Completado |
| Gunicorn y Nginx | ✅ Completado |
| Gestión mediante systemd | ✅ Completado |
| Endurecimiento del servicio | ✅ Completado |
| Contenerización con Docker | ✅ Completado |
| Docker Compose | ✅ Completado |
| Integración continua (CI) | ✅ Completado |
| Mejoras de monitorización | ⏳ Pendiente |
| Automatización con Bash y Python | ⏳ Pendiente |
| Despliegue continuo (CD) | 🔜 Futuro |
| Despliegue en cloud | 🔜 Futuro |

## 📚 Objetivo profesional

Este laboratorio forma parte de un itinerario práctico de aprendizaje orientado a la administración de sistemas, infraestructura IT, middleware y tecnologías DevOps.

El objetivo es demostrar conocimientos mediante implementaciones funcionales, configuración de servicios, resolución de problemas, automatización, contenerización y aplicación de buenas prácticas de seguridad.

El repositorio sirve como portfolio técnico para documentar el trabajo realizado y facilitar su evaluación por parte de profesionales y reclutadores del sector IT.

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT.
