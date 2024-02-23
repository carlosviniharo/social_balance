## Wait for the Database to be ready
#while ! nc -z db 5432; do
#    sleep 1
#done

# Initialize Django
python manage.py makemigrations
python manage.py migrate

# Start Django
apache2ctl -D FOREGROUND
