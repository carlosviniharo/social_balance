#!/bin/sh
# Wait for the Database to be ready
while ! nc -z db 5432; do
    sleep 1
done

# Initialize Django
python manage.py makemigrations
python manage.py migrate

# Start Django
python manage.py runserver 0.0.0.0:8000