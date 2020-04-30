FROM python:3

WORKDIR /code

COPY requirements ./requirements

RUN pip install --no-cache-dir -r ./requirements/base.txt

CMD python manage.py runserver