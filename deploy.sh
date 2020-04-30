#!/bin/bash
pwd

docker-compose build && docker-compose up -d
docker-compose run --rm backend sh -c "python manage.py migrate && python manage.py createsuperuser"
docker-compose ps
docker-compose logs -f backend