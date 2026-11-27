# Configuración Gunicorn para Docker

bind = "0.0.0.0:8000"

workers = 2

# Access logs a stdout
accesslog = "-"

# Error logs a stderr
errorlog = "-"

loglevel = "info"

capture_output = True

control_socket_disable = True
