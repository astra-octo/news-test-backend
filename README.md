# DEPLOY
## backend
1) create env files in \_\___docker_files__\_\_ 
    - .env.backend:
        - DB_USER - database user name
        - DB_NAME - database name
        - DB_PASSWORD - database password
    - .env.database:
        - POSTGRES_PASSWORD
        - POSTGRES_USER
        - POSTGRES_DB
2) run docker ( `docker-compose build && docker-compose up -d` ). Starting on localhost:8888
3) run migrations `docker-compose run --rm backend sh -c "python manage.py migrate"`
4) create superuser `docker-compose run --rm backend sh -c "python manage.py createsuperuser"`
