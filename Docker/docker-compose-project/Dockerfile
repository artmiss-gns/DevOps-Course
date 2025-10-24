# FROM python:3.14.0b3-alpine3.21
FROM python:3.12.0b1-slim-buster

RUN mkdir /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . .

CMD uvicorn app.main:app --reload --port=8001 --host=0.0.0.0
