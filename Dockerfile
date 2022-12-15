FROM python:3.11.1

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get -y install default-libmysqlclient-dev \
  && apt-get clean

COPY requirements.txt ./
RUN pip install --upgrade pip \
  && pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . .
