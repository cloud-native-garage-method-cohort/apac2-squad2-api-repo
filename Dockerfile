FROM ubuntu:16.04
FROM python:3
# FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
# FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app/src/ .
EXPOSE 5000
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "python", "./app.py" ]