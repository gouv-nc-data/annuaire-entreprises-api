FROM bitnami/python:3.12-debian-12

ENV HOST=0.0.0.0
ENV LISTEN_PORT=8080
EXPOSE 8080
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app ./app
COPY alembic.ini .
COPY alembic ./alembic

CMD ["fastapi", "run", "--workers", "1", "app/main.py", "--proxy-headers", "--port", "8080"]
