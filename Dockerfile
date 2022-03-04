FROM python:3.9.5

WORKDIR usr/src/template-flask
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .