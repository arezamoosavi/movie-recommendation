FROM python:3.8.0-alpine
# FROM python:3.7.6-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add make gcc python3-dev musl-dev libffi-dev linux-headers g++ \
  gfortran py-pip build-base wget freetype-dev libpng-dev openblas-dev binutils cython libstdc++

RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install --no-cache-dir pandas==0.25.3

RUN mkdir -p /src

RUN addgroup -S xuzer && adduser -S -G xuzer xuzer

ADD ./src /src
WORKDIR /src

EXPOSE 5000

CMD ["python", "app.py"]
