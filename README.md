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
| systemd | Gestión y supervisión del servicio |
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
├── tests/
│   └── test_app.py
│
├── logs/                  # Registros generados en ejecución
│   ├── app.log
│   ├── gunicorn-access.log
│   └── gunicorn-error.log
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
python -m pip install -r requirements.txt
```

### Configuración

Los parámetros del servidor se encuentran en `gunicorn.conf.py`:

```python
bind = "127.0.0.1:8000"

workers = 2

accesslog = "logs/gunicorn-access.log"
errorlog = "logs/gunicorn-error.log"

loglevel = "info"

capture_output = True
```

Características principales:

- Dos procesos worker.
- Escucha en la interfaz local `127.0.0.1`.
- Puerto 8000.
- Registro independiente de accesos y errores.
- Captura de la salida estándar y de errores.

### Ejecución manual

```bash
gunicorn --config gunicorn.conf.py "app:create_app()"
```

Gunicorn utiliza la Application Factory de Flask para crear la instancia de la aplicación.

## 🌐 Nginx como proxy inverso

Se ha instalado y configurado **Nginx** como servidor web y proxy inverso.

La arquitectura permite recibir las peticiones HTTP en el puerto 80 y reenviarlas a Gunicorn, que escucha en el puerto 8000 de la interfaz local.

### Configuración

Archivo:

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

El sitio se habilita mediante un enlace simbólico en:

```text
/etc/nginx/sites-enabled/
```

### Validación

Comprobar la sintaxis:

```bash
sudo nginx -t
```

Recargar la configuración:

```bash
sudo systemctl reload nginx
```

Comprobar el endpoint:

```bash
curl -i http://127.0.0.1/health
```

La respuesta esperada es HTTP 200:

```json
{
  "status": "ok"
}
```

## ⚙️ Gestión del servicio con systemd

Se ha configurado un servicio de **systemd** para gestionar Gunicorn como un servicio del sistema.

Archivo:

```text
/etc/systemd/system/cloud-middleware-lab.service
```

Configuración principal:

```ini
[Unit]
Description=Cloud Middleware Lab - Gunicorn
After=network.target

[Service]
User=cloudlab
Group=cloudlab
WorkingDirectory=/home/mario/proyectos/cloud-middleware-devops

ExecStart=/home/mario/proyectos/cloud-middleware-devops/.venv/bin/gunicorn --config /home/mario/proyectos/cloud-middleware-devops/gunicorn.conf.py "app:create_app()"

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Gestión del servicio

Recargar la configuración de systemd:

```bash
sudo systemctl daemon-reload
```

Iniciar y habilitar el servicio:

```bash
sudo systemctl enable --now cloud-middleware-lab
```

Consultar su estado:

```bash
sudo systemctl status cloud-middleware-lab
```

Reiniciar:

```bash
sudo systemctl restart cloud-middleware-lab
```

Detener:

```bash
sudo systemctl stop cloud-middleware-lab
```

Consultar los registros:

```bash
sudo journalctl -u cloud-middleware-lab
```

El servicio está configurado para iniciarse automáticamente con el sistema y reiniciarse si se produce un fallo.

## 🔐 Seguridad y permisos

Se han aplicado medidas de aislamiento y endurecimiento del servicio para reducir los privilegios y limitar el acceso a los recursos del sistema.

### Usuario dedicado

La aplicación se ejecuta mediante un usuario específico:

```text
cloudlab
```

Este usuario evita ejecutar Gunicorn con la cuenta personal o con privilegios de root.

Se han configurado los permisos necesarios para que el servicio pueda:

- Leer el código de la aplicación.
- Acceder a la configuración de Gunicorn.
- Ejecutar el binario del entorno virtual.
- Escribir en el directorio de registros.

### Endurecimiento de systemd

Se han aplicado directivas de seguridad adicionales mediante un archivo de configuración complementario:

```text
/etc/systemd/system/cloud-middleware-lab.service.d/override.conf
```

Entre las medidas aplicadas se encuentran:

- `NoNewPrivileges`: impide adquirir nuevos privilegios.
- `UMask`: controla los permisos predeterminados de los archivos creados por el servicio.
- `PrivateTmp`: proporciona un directorio temporal aislado.
- `ProtectSystem=full`: restringe la escritura en partes del sistema de archivos.
- `ProtectKernelTunables`: protege los parámetros del kernel.
- `ProtectKernelModules`: impide cargar módulos del kernel.
- `ProtectKernelLogs`: restringe el acceso a los registros del kernel.
- `ProtectControlGroups`: protege la jerarquía de grupos de control.
- `ProtectHostname`: impide modificar el nombre del sistema.
- `ProtectClock`: impide modificar el reloj del sistema.
- `RestrictSUIDSGID`: restringe la creación de archivos SUID/SGID.
- `LockPersonality`: restringe los cambios de personalidad del proceso.
- `PrivateDevices`: limita el acceso a dispositivos.
- `ProtectProc`: restringe la visibilidad del árbol de procesos.
- `ProcSubset`: limita la información disponible en `/proc`.
- `RestrictNamespaces`: limita la creación de espacios de nombres.
- `RestrictRealtime`: restringe el acceso a la planificación en tiempo real.
- `SystemCallArchitectures`: limita las arquitecturas de llamadas al sistema permitidas.
- `CapabilityBoundingSet`: elimina las capacidades adicionales del servicio.
- `AmbientCapabilities`: no concede capacidades adicionales.
- `RestrictAddressFamilies`: limita las familias de direcciones de red permitidas.
- `MemoryDenyWriteExecute`: restringe la creación de memoria ejecutable y escribible simultáneamente.

### Evaluación de seguridad

La configuración se ha evaluado mediante:

```bash
sudo systemd-analyze security cloud-middleware-lab.service
```

Resultado obtenido:

- Nivel de exposición: **3.1 OK**.

Esta puntuación corresponde a la evaluación de systemd y no constituye una auditoría completa de seguridad de la aplicación o del sistema.

## 🔄 Arquitectura del despliegue

El flujo de una petición HTTP es el siguiente:

```text
          CLIENTE
             |
             | HTTP :80
             v
       +-----------+
       |   NGINX   |
       |  Proxy    |
       |  inverso  |
       +-----------+
             |
             | HTTP
             | 127.0.0.1:8000
             v
       +-----------+
       | GUNICORN  |
       | WSGI      |
       | 2 workers |
       +-----------+
             |
             v
       +-----------+
       |   FLASK   |
       | Aplicación|
       +-----------+
             |
             v
       +-----------+
       |  ENDPOINT |
       | /health   |
       +-----------+
```

**Responsabilidades de cada componente:**

| Componente | Responsabilidad |
|---|---|
| Nginx | Recepción de peticiones HTTP y proxy inverso |
| Gunicorn | Servidor WSGI y gestión de procesos worker |
| Flask | Lógica y rutas de la aplicación |
| systemd | Gestión, supervisión y arranque del servicio |
| Logging | Registro de actividad y errores |

El despliegue se ha validado tanto mediante una conexión directa a Gunicorn como a través de Nginx.

## 📊 Estado actual del proyecto

| Área | Estado |
|---|---|
| Entorno Linux y Python | ✅ Completado |
| Entorno virtual | ✅ Completado |
| Aplicación Flask | ✅ Completado |
| Application Factory y Blueprints | ✅ Completado |
| Configuración por entornos | ✅ Completado |
| Endpoint Health Check | ✅ Completado |
| Logging y rotación de registros | ✅ Completado |
| Gestión global de excepciones | ✅ Completado |
| Pruebas automatizadas | ✅ Completado |
| Servidor WSGI Gunicorn | ✅ Completado |
| Proxy inverso Nginx | ✅ Completado |
| Servicio systemd | ✅ Completado |
| Usuario dedicado | ✅ Completado |
| Endurecimiento de systemd | ✅ Completado |
| Validación del despliegue | ✅ Completado |

## 🗺️ Hoja de ruta

El proyecto continuará evolucionando progresivamente:

| Área | Estado |
|---|---|
| Entorno Linux y Python | ✅ Completado |
| Aplicación Flask modular | ✅ Completado |
| Pruebas automatizadas y cobertura | ✅ Completado |
| Logging y gestión de excepciones | ✅ Completado |
| Gunicorn como servidor WSGI | ✅ Completado |
| Nginx como proxy inverso | ✅ Completado |
| Gestión mediante systemd | ✅ Completado |
| Endurecimiento del servicio | ✅ Completado |
| Logging estructurado en JSON | ⏳ Pendiente |
| Mejoras de monitorización | ⏳ Pendiente |
| Contenerización con Docker | ⏳ Pendiente |
| Integración y despliegue continuo (CI/CD) | ⏳ Pendiente |
| Automatización con Bash y Python | ⏳ Pendiente |
| Despliegue en cloud | 🔜 Futuro |

## 📚 Objetivo profesional

Este laboratorio forma parte de un itinerario práctico de aprendizaje orientado a la administración de sistemas, infraestructura IT, middleware y tecnologías DevOps.

El objetivo es documentar y demostrar conocimientos mediante implementaciones funcionales, configuración de servicios, resolución de problemas y aplicación de buenas prácticas.

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT.
