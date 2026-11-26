# Configuración de Gunicorn

bind = "127.0.0.1:8000"

workers = 2

accesslog = "logs/gunicorn-access.log"
errorlog = "logs/gunicorn-error.log"

loglevel = "info"

capture_output = True
