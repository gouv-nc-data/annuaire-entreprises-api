FROM bitnami/python:3.12-debian-12

ENV HOST=0.0.0.0
ENV LISTEN_PORT=8000
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -U -r requirements.txt

COPY app ./app
COPY alembic.ini .
COPY alembic ./alembic

CMD ["fastapi", "run", "app/main.py"]
