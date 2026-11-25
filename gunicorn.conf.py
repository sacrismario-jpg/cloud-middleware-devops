# Configuración de Gunicorn

bind = "127.0.0.1:8000"

workers = 2

accesslog = "/home/mario/proyectos/cloud-middleware-devops/logs/gunicorn-access.log"
errorlog = "/home/mario/proyectos/cloud-middleware-devops/logs/gunicorn-error.log"

loglevel = "info"

capture_output = True
