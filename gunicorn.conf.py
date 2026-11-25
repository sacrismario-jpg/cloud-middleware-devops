# Configuracion de Gunicorn

bind = "127.0.0.1:8000"

workers = 2

accesslog = "_"
errorlog = "_"
loglevel = "info"

capture_output = True
