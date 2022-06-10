#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py makemigrations
python manage.py migrate
echo "======================================"
echo "SAFRIZAL: YOUR PROJECT IS READY TO GO!"
echo "======================================"