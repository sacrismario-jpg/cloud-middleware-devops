FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LOG_TO_STDOUT=1

WORKDIR /app

RUN groupadd --system appgroup && \
    useradd --system --gid appgroup --create-home appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY gunicorn.docker.conf.py .

RUN mkdir -p logs && \
    chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)" || exit 1

CMD ["gunicorn", "--config", "gunicorn.docker.conf.py", "app:create_app()"]
