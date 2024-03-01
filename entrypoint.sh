#!/bin/sh

echo "Apply migrations"

echo "Current directory:"
pwd
ls -la

echo "Checking ciphers_project directory:"
cd ./ciphers_project
ls -la

# cd ./ciphers_project
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

exec "$@"


