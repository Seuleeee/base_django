FROM python:3.11.1-slim-buster AS  base

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get -y install netcat gcc && \
    apt-get -y install default-libmysqlclient-dev && \
    apt-get clean \

FROM python:3.11.1-slim-buster as stage1

COPY . .
COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN mkdir -p logs




