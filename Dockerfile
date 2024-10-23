###########
# BUILDER #
###########

FROM python:3.10.9-alpine3.17 as builder

WORKDIR /home/app/web/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY . .


COPY ./requirements.txt .
RUN pip install -r requirements.txt