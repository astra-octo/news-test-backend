FROM python:3

WORKDIR /code

COPY requirements ./

RUN pip install --no-cache-dir -r requirements/base.txt

