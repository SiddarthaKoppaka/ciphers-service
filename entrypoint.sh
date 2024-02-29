#!/bin/sh

echo "Apply migrations"

cd ./ciphers_project
python manage.py migrate
python manage.py runserver

exec"$@"