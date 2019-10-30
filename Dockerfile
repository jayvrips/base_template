FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org pipenv
RUN apt-get update
RUN apt-get install -y gcc libpq-dev postgresql-client
