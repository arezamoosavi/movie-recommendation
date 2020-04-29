FROM python:3.7.6-alpine
# FROM python:3.7.6-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add  --no-cache --virtual build-dependencies libc-dev build-base \
python3-dev libxml2 libxml2-dev libxslt libxslt-dev libjpeg-turbo-dev zlib-dev musl-dev \
freetype-dev libpng-dev openblas-dev libffi-dev gcc libressl-dev
RUN addgroup -S xuzer && adduser -S -G xuzer xuzer

RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir -p /src

# ADD ./src /src
WORKDIR /src

EXPOSE 5000

CMD gunicorn -w 4 app:app -b :5000
