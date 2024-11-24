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

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=fr_FR.UTF-8

ENV LANG fr_FR.UTF-8

CMD ["fastapi", "run", "--workers", "1", "app/main.py", "--proxy-headers", "--port", "8080"]
