FROM python:3.12-slim

ENV HOST=0.0.0.0
ENV LISTEN_PORT=8000
EXPOSE 8000

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -U -r requirements.txt

COPY app/* .

CMD ["fastapi", "run", "main.py", "--port", "8080"]